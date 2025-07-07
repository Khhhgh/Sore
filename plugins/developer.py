from pyrogram import Client
from pyrogram.types import Message
from config import developer
import re
from database import get_db_general_rtb, del_db_general_rtb, set_db_general_rtb


async def check_username(m, c):
    if bool(re.search(r"\D", m.text)) is True:
        c_id = m.text
    else:
        c_id = int(m.text)
    try:
        a = await c.get_chat(c_id)
        if a.title is not None:
            full_id = a.id
            str_chat = f"{full_id}"
            chat_id = str_chat[4:]
            chat_name = a.title
            if a.username is None:
                chat_username = "لايوجد"
            else:
                chat_username = f"@{a.username}"
            # link = f"https://t.me/c/{chat_id}/2"
        else:
            chat_id = a.id
            chat_name = a.first_name
            if a.username is None:
                chat_username = "لايوجد"
            else:
                chat_username = f"@{a.username}"
            # link = f"tg://user?id={chat_id}"

    except Exception as e:
        chat_id = c_id
        chat_name = "id " + str(c_id)
        chat_username = "لايوجد"
        print(e)
    return chat_id, chat_name, chat_username


########################################################################################################################
########################################################################################################################

async def developersrep(m: Message):
    try:
        if get_db_general_rtb("developer") is None:
            set_db_general_rtb("developer", m.reply_to_message.from_user.id,
                               m.reply_to_message.from_user.first_name)
            await m.reply_text(f"✪ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مطور بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(m.reply_to_message.from_user.id)
            return
        else:
            for dv in get_db_general_rtb("developer"):
                if m.reply_to_message.from_user.id == dv[0]:
                    await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) مطور بالفعل\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_general_rtb("developer", m.reply_to_message.from_user.id,
                               m.reply_to_message.from_user.first_name)
            await m.reply_text(f"✪ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مطور بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(m.reply_to_message.from_user.id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def developersuser(c: Client, m: Message):
    m.text = m.text[9:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_general_rtb("developer") is None:
            set_db_general_rtb("developer", chat_id_foruser, chat_name_foruser)
            await m.reply_text(f"✪ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مطور بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(chat_id_foruser)
            return
        else:
            for dv in get_db_general_rtb("developer"):
                if chat_id_foruser == dv[0]:
                    await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) مطور بالفعل\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_general_rtb("developer", chat_id_foruser, chat_name_foruser)
            await m.reply_text(f"✪ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مطور بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(chat_id_foruser)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def undevelopersrep(m: Message):
    try:
        if get_db_general_rtb("developer") is None:
            await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مطور اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("developer"):
                if m.reply_to_message.from_user.id == dv[0]:
                    del_db_general_rtb("developer", m.reply_to_message.from_user.id)
                    await m.reply_text(f"✪ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المطورين بنجاح\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    developer.remove(m.reply_to_message.from_user.id)
                    return
            await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مطور اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def undeveloperuser(c: Client, m: Message):
    m.text = m.text[11:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_general_rtb("developer") is None:
            await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مطور اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("developer"):
                if chat_id_foruser == dv[0]:
                    del_db_general_rtb("developer", chat_id_foruser)
                    await m.reply_text(f"✪ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من المطورين بنجاح\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    developer.remove(chat_id_foruser)
                    return
            await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مطور اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


########################################################################################################################
########################################################################################################################

async def seconddevelopersrep(m: Message):
    try:
        if get_db_general_rtb("secdeveloper") is None:
            set_db_general_rtb("secdeveloper", m.reply_to_message.from_user.id,
                               m.reply_to_message.from_user.first_name)
            await m.reply_text(f"✪ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مطور ثانوي بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(m.reply_to_message.from_user.id)
            return
        else:
            for dv in get_db_general_rtb("secdeveloper"):
                if m.reply_to_message.from_user.id == dv[0]:
                    await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) مطور ثانوي بالفعل\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_general_rtb("secdeveloper", m.reply_to_message.from_user.id,
                               m.reply_to_message.from_user.first_name)
            await m.reply_text(f"✪ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مطور ثانوي بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(m.reply_to_message.from_user.id)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def seconddevelopersuser(c: Client, m: Message):
    m.text = m.text[15:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_general_rtb("secdeveloper") is None:
            set_db_general_rtb("secdeveloper", chat_id_foruser, chat_name_foruser)
            await m.reply_text(f"✪ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مطور ثانوي بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(chat_id_foruser)
            return
        else:
            for dv in get_db_general_rtb("secdeveloper"):
                if chat_id_foruser == dv[0]:
                    await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) مطور ثانوي بالفعل\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_general_rtb("secdeveloper", chat_id_foruser, chat_name_foruser)
            await m.reply_text(f"✪ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مطور ثانوي بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(chat_id_foruser)

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def secondundevelopersrep(m: Message):
    try:
        if get_db_general_rtb("secdeveloper") is None:
            await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مطور ثانوي اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("secdeveloper"):
                if m.reply_to_message.from_user.id == dv[0]:
                    del_db_general_rtb("secdeveloper", m.reply_to_message.from_user.id)
                    await m.reply_text(f"✪ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المطورين الثانويين بنجاح\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    developer.remove(m.reply_to_message.from_user.id)
                    return
            await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مطور ثانوي اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def secondundeveloperuser(c: Client, m: Message):
    m.text = m.text[17:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_general_rtb("secdeveloper") is None:
            await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مطور ثانوي اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("secdeveloper"):
                if chat_id_foruser == dv[0]:
                    del_db_general_rtb("secdeveloper", chat_id_foruser)
                    await m.reply_text(f"✪ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من المطورين الثانويين بنجاح\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    developer.remove(chat_id_foruser)
                    return
            await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مطور ثانوي اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

########################################################################################################################
########################################################################################################################


async def genspecialrep(m: Message):
    try:
        if get_db_general_rtb("genspecial") is None:
            set_db_general_rtb("genspecial", m.reply_to_message.from_user.id,
                               m.reply_to_message.from_user.first_name)
            await m.reply_text(f"✪ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مميز عام بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("genspecial"):
                if m.reply_to_message.from_user.id == dv[0]:
                    await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) مميز عام بالفعل\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_general_rtb("genspecial", m.reply_to_message.from_user.id,
                               m.reply_to_message.from_user.first_name)
            await m.reply_text(f"✪ تم رفع العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) مميز عام بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def genspecialuser(c: Client, m: Message):
    m.text = m.text[13:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_general_rtb("genspecial") is None:
            set_db_general_rtb("genspecial", chat_id_foruser, chat_name_foruser)
            await m.reply_text(f"✪ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مميز عام بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            developer.append(chat_id_foruser)
            return
        else:
            for dv in get_db_general_rtb("genspecial"):
                if chat_id_foruser == dv[0]:
                    await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) مميز عام بالفعل\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            set_db_general_rtb("genspecial", chat_id_foruser, chat_name_foruser)
            await m.reply_text(f"✪ تم رفع العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) مميز عام بنجاح\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def ungenspecialrep(m: Message):
    try:
        if get_db_general_rtb("genspecial") is None:
            await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مميز عام اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("genspecial"):
                if m.reply_to_message.from_user.id == dv[0]:
                    del_db_general_rtb("genspecial", m.reply_to_message.from_user.id)
                    await m.reply_text(f"✪ تم تنزيل العضو [{m.reply_to_message.from_user.first_name}]"
                                       f"(tg://user?id={m.reply_to_message.from_user.id}) من المميز عامين بنجاح\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"✪ العضو [{m.reply_to_message.from_user.first_name}]"
                               f"(tg://user?id={m.reply_to_message.from_user.id}) غير مميز عام اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return


async def ungenspecialuser(c: Client, m: Message):
    m.text = m.text[15:]
    result = await check_username(m, c)
    chat_id_foruser = result[0]
    chat_name_foruser = result[1]
    try:
        if get_db_general_rtb("genspecial") is None:
            await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مميز عام اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")
            return
        else:
            for dv in get_db_general_rtb("genspecial"):
                if chat_id_foruser == dv[0]:
                    del_db_general_rtb("genspecial", chat_id_foruser)
                    await m.reply_text(f"✪ تم تنزيل العضو [{chat_name_foruser}]"
                                       f"(tg://user?id={chat_id_foruser}) من المميز عامين بنجاح\n🇾🇪",
                                       reply_to_message_id=m.message_id, parse_mode="Markdown")
                    return
            await m.reply_text(f"✪ العضو [{chat_name_foruser}]"
                               f"(tg://user?id={chat_id_foruser}) غير مميز عام اصلا\n🇾🇪",
                               reply_to_message_id=m.message_id, parse_mode="Markdown")

    except Exception as e:
        await m.reply_text(str(e) + "\n\n" +
                           "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                           reply_to_message_id=m.message_id, parse_mode="Markdown")
        return

########################################################################################################################
########################################################################################################################
