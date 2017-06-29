package com.example.blair.databasesync2;

import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;

public class MainActivity extends AppCompatActivity {

    private static final String url = "jdbc:mysql://sql9.freemysqlhosting.net/sql9182609";
    //private static final String url = "jdbc:mysql://192.168.2.23:3306/fitness";
    private static final String user = "sql9182609";
    private static final String pass = "AN2ffn1RAh";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        testDB();
    }

    public void testDB(){
        TextView tv = (TextView)this.findViewById(R.id.tv1);

        try {

            StrictMode.ThreadPolicy policy =
                    new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);

            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(url, user, pass);

            String result = "Database connection successful!\n";
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery("select * from log");
            ResultSetMetaData rsmd = rs.getMetaData();

            while(rs.next()){
                result += rsmd.getColumnName(1) + ": " + rs.getInt(1) + "\n";
                result += rsmd.getColumnName(2) + ": " + rs.getString(2) + "\n";
                result += rsmd.getColumnName(3) + ": " + rs.getInt(3) + "\n";
            }
            tv.setText(result);

        }

        catch (ClassNotFoundException e) {
            e.printStackTrace();
            tv.setText(e.toString());
        }

        catch (SQLException e) {
            e.printStackTrace();
            tv.setText(e.toString());
        }

    }
}
