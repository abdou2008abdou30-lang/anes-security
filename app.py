import streamlit as st

st.set_page_config(page_title="أمن التخدير - تحليل الأرقام", page_icon="📱")

st.title("🛡️ موقع أمن التخدير")
st.subheader("تحليل معلومات رقم الهاتف (الدولة، المكان، ونوع الشريحة)")

# إدخال رقم الهاتف
phone_input = st.text_input("أدخل رقم الهاتف (مع رمز الدولة، مثال: +213...):", "")

if st.button("تحليل الرقم"):
    if phone_input:
        st.success("تم تحليل بيانات الرقم بنجاح:")
        
        # تحليل الدولة والمكان ونوع الشريحة
        if phone_input.startswith("+213") or phone_input.startswith("213") or phone_input.startswith("0"):
            st.info("🌍 الدولة: الجزائر (Algeria)")
            
            # تحديد نوع الشريحة والمتعامل
            if "05" in phone_input or "5" in phone_input:
                st.write("📶 نوع الشريحة / المتعامل: Ooredoo الجزائر")
                st.write("🏷️ هوية الخط: خط هاتف محمول (مسبق الدفع / فواتير)")
            elif "06" in phone_input or "6" in phone_input:
                st.write("📶 نوع الشريحة / المتعامل: Mobilis (موبيليس)")
                st.write("🏷️ هوية الخط: خط هاتف محمول (اتصالات الجزائر)")
            elif "07" in phone_input or "7" in phone_input:
                st.write("📶 نوع الشريحة / المتعامل: Djezzy (جيزي)")
                st.write("🏷️ هوية الخط: خط هاتف محمول (جيزي)")
            else:
                st.write("📶 نوع الشريحة: خط هاتف محمول وطني")
                
            # تحليل الولاية أو المنطقة
            if "31" in phone_input or "031" in phone_input:
                st.write("📍 المكان الجغرافي (الولاية): قسنطينة (Constantine)")
            elif "21" in phone_input or "021" in phone_input:
                st.write("📍 المكان الجغرافي (الولاية): الجزائر العاصمة (Algiers)")
            elif "41" in phone_input or "041" in phone_input:
                st.write("📍 المكان الجغرافي (الولاية): وهران (Oran)")
            elif "29" in phone_input or "029" in phone_input:
                st.write("📍 المكان الجغرافي (الولاية): ورقلة / الجنوب الشرقي")
            else:
                st.write("📍 المكان الجغرافي: تغطية وطنية عامة (غير محدد بولاية معينة)")
                
        elif phone_input.startswith("+20") or phone_input.startswith("20"):
            st.info("🌍 الدولة: مصر (Egypt)")
            st.write("📶 نوع الشريحة: شريحة اتصالات مصرية")
            st.write("📍 المكان الجغرافي: جمهورية مصر العربية")
        elif phone_input.startswith("+966") or phone_input.startswith("966"):
            st.info("🌍 الدولة: المملكة العربية السعودية (Saudi Arabia)")
            st.write("📶 نوع الشريحة: شريحة اتصالات سعودية")
            st.write("📍 المكان الجغرافي: المملكة العربية السعودية")
        else:
            st.warning("الرجاء إدخال رقم هاتف صحيحة ومبتدئ بررمز دولي معروف.")
    else:
        st.error("الرجاء إدخال رقم الهاتف في الخانة المخصصة أولاً!")
import streamlit as st

st.set_page_config(page_title="أمن التخدير - تحديد الموقع الجغرافي", page_icon="🌍")

st.title("🛡️ موقع أمن التخدير")
st.subheader("تحليل ومعرفة مكان الدولة والولاية من رقم الهاتف")

# إدخال رقم الهاتف
phone_input = st.text_input("أدخل رقم الهاتف (مع رمز الدولة، مثال: +213...):", "")

if st.button("تحديد الموقع"):
    if phone_input:
        st.success("تم تحليل بيانات الرقم بنجاح:")
        
        # تحليل الدولة والمكان بناءً على البادئة
        if phone_input.startswith("+213") or phone_input.startswith("213"):
            st.info("🌍 الدولة: الجزائر (Algeria)")
            
            # تحليل مكاني مبدئي بناءً على رموز الولايات (مثال لأكواد الهاتف الثابت أو المتنقل)
            if "31" in phone_input or "031" in phone_input:
                st.write("📍 المنطقة / الولاية المحتملة: قسنطينة (Constantine)")
            elif "21" in phone_input or "021" in phone_input:
                st.write("📍 المنطقة / الولاية المحتملة: الجزائر العاصمة (Algiers)")
            elif "41" in phone_input or "041" in phone_input:
                st.write("📍 المنطقة / الولاية المحتملة: وهران (Oran)")
            elif "29" in phone_input or "029" in phone_input:
                st.write("📍 المنطقة / الولاية المحتملة: ورقلة / الجنوب الشرقي (Ouargla Region)")
            else:
                st.write("📍 المنطقة: شبكة الهاتف النقال الوطني (تغطية وطنية عامة)")
                
        elif phone_input.startswith("+20") or phone_input.startswith("20"):
            st.info("🌍 الدولة: مصر (Egypt)")
            st.write("📍 المنطقة: جمهورية مصر العربية")
        elif phone_input.startswith("+966") or phone_input.startswith("966"):
            st.info("🌍 الدولة: المملكة العربية السعودية (Saudi Arabia)")
            st.write("📍 المنطقة: المملكة العربية السعودية")
        else:
            st.warning("الرجاء إدخال رقم هاتف صحيحة ومبتدئ برمز دولي معروف.")
    else:
        st.error("الرجاء إدخال رقم الهاتف في الخانة المخصصة أولاً!")
import streamlit as st

st.set_page_config(page_title="أمن التخدير - تحليل الأرقام", page_icon="📱")

st.title("🛡️ موقع أمن التخدير")
st.subheader("تحليل ومعلومات أرقام الهواتف")

# إدخال رقم الهاتف
phone_input = st.text_input("أدخل رقم الهاتف (مثال: +213...):", "")

if st.button("تحليل الرقم"):
    if phone_input:
        st.success("تم تحليل الرقم بنجاح:")
        
        # تحليل مبدئي بناءً على الرموز المعيارية
        if phone_input.startswith("+213") or phone_input.startswith("0"):
            st.info("🌍 الدولة: الجزائر (Algeria)")
            
            # تحليل الجهة المشغلة (مثال توضيحي للشركات الجزائرية)
            if "05" in phone_input or "5" in phone_input:
                st.write("📶 المتعامل: Ooredoo الجزائر")
            elif "06" in phone_input or "6" in phone_input:
                st.write("📶 المتعامل: Mobilis")
            elif "07" in phone_input or "7" in phone_input:
                st.write("📶 المتعامل: Djezzy")
            else:
                st.write("📶 نوع الشريحة: خط هاتف محمول جزائري")
        else:
            st.warning("الرجاء إدخال رقم هاتف صحيح يبدأ بالرمز الدولي المناسب.")
    else:
        st.error("الرجاء إدخال رقم هاتف أولاً!")
