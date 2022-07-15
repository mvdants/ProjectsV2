import 'package:flutter/material.dart';

class TelaCreateJob extends StatefulWidget {
  const TelaCreateJob({Key? key}) : super(key: key);

  @override
  State<TelaCreateJob> createState() => _TelaCreateJobState();
}

class _TelaCreateJobState extends State<TelaCreateJob> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.teal,
        title: const Text("Creating Job Offer"),
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(32),
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.only(top: 32),
                child: Image.asset("images/create_job_colored.png"),
              ),
              const Padding(
                padding: EdgeInsets.only(top: 32),
                child: TextField(
                  showCursor: false,
                  decoration: InputDecoration(
                    labelText: "Job Tittle",
                    labelStyle: TextStyle(
                      color: Colors.blueGrey
                    ),
                    enabledBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.grey)
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: BorderSide(color: Colors.tealAccent)
                    ),
                  ),
                ),
              ),
              const Padding(
                padding: EdgeInsets.only(top: 32),
                child: TextField(
                  textAlign: TextAlign.justify,
                  maxLines: 5,
                  showCursor: false,
                  decoration: InputDecoration(
                    alignLabelWithHint: true,
                    floatingLabelAlignment: FloatingLabelAlignment.start,
                    labelText: "Job Description",
                    labelStyle: TextStyle(
                        color: Colors.blueGrey
                    ),
                    enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: Colors.grey)
                    ),
                    focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: Colors.tealAccent)
                    ),
                  ),
                ),
              ),
              const Padding(
                padding: EdgeInsets.only(top: 64),
                child: TextField(
                  keyboardType: TextInputType.numberWithOptions(decimal: true),
                  showCursor: false,
                  decoration: InputDecoration(
                    suffixText: "R\$",
                    labelText: "Gratification",
                    labelStyle: TextStyle(
                        color: Colors.blueGrey
                    ),
                    enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: Colors.grey)
                    ),
                    focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: Colors.tealAccent)
                    ),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(top: 64),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    OutlinedButton(
                      child: const Text(
                        "Create",
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 28,
                        ),
                      ),
                      style: OutlinedButton.styleFrom(
                        primary: Colors.white,
                        backgroundColor: Colors.teal,
                        shape: const RoundedRectangleBorder(
                            borderRadius: BorderRadius.all(
                                Radius.circular(20)
                            )
                          ),
                        ),
                      onPressed: (){},
                    ),
                  ],
                )
              )
            ],
          ),
        ),
      )

    );
  }
}
