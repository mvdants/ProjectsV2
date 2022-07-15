import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:fastlink/TelaUser.dart';
import 'package:fastlink/TelaConfig.dart';
import 'package:fastlink/TelaCreateJob.dart';
import 'package:fastlink/TelaSearchingJob.dart';
import 'package:fastlink/TelaMessage.dart';


class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {

  void _abrirUser(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => TelaUser()));
  }

  void _abrirConfig(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => TelaConfig()));
  }

  void _abrirCreateJob(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => TelaCreateJob()));
  }

  void _abrirSearchingJob(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => TelaSearchingJob()));
  }

  void _abrirMessage(){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => TelaMessage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(

      appBar: AppBar(
        title: const Text("Fast Job"),
        backgroundColor: Colors.teal,
      ),
      body: Container(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          //crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Padding(
                padding: const EdgeInsets.only(top: 16),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    GestureDetector(
                      onTap: _abrirUser,
                      child: Image.asset("images/user.png"),
                    ),
                    GestureDetector(
                      onTap: _abrirSearchingJob,
                      child: Image.asset("images/job.png"),
                    )
                  ],
                ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 32),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  GestureDetector(
                    onTap: _abrirCreateJob,
                    child: Image.asset("images/create_job.png"),
                  ),
                  GestureDetector(
                    onTap: _abrirConfig,
                    child: Image.asset("images/config.png"),
                  )
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(top: 32),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  GestureDetector(
                    onTap: _abrirMessage,
                    child: Image.asset("images/mail-2.png"),
                  )
                ],
              ),
            ),
            const Padding(
                padding: EdgeInsets.only(top: 64),
                child: Text(
                  "Waskor Company",
                  style: TextStyle(
                    fontSize: 14,
                    fontStyle: FontStyle.italic,
                  ),
                ),
            ),
          ],
        ),
      ),
    );
  }
}
