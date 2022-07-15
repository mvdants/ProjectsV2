import 'package:flutter/material.dart';

class TelaMessage extends StatefulWidget {
  const TelaMessage({Key? key}) : super(key: key);

  @override
  State<TelaMessage> createState() => _TelaMessageState();
}

class _TelaMessageState extends State<TelaMessage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Message"),
        backgroundColor: Colors.teal,
      ),
    );
  }
}
