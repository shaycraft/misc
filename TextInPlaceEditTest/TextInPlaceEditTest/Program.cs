using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace TextInPlaceEditTest
{
    class Program
    {
        private static int[] FindNewlines(Stream s)
        {
            List<int> tmp = new List<int>();
            int curr_pos = 0;
            int read_chunk = 100;
            byte[] b = new byte[read_chunk];

            while ((s.Read(b, (int)s.Position, read_chunk)) > 0)
            {
                Console.WriteLine(b.ToString());
            }

            return null;
        }

        static void Main(string[] args)
        {
            foreach (var file in (new DirectoryInfo("..\\..\\").EnumerateFiles()))
            {
                Console.WriteLine(String.Format("{0},{1}", file.Name, file.FullName));
            }

            FileStream fs = null;
            try
            {
                String fileName = Path.Combine("..\\..\\", "samplefile.txt");
                fs = new FileStream(fileName, FileMode.Open, FileAccess.ReadWrite);
            }
            catch (IOException ex)
            {
                Console.Error.WriteLine("ERROR: {0}", ex.Message);
            }

            StreamWriter wr = new StreamWriter(fs);
            StreamReader rd = new StreamReader(fs);
            fs.Seek(0, SeekOrigin.Begin);
            FindNewlines(fs);
            //Console.WriteLine(rd.ReadLine());
            //wr.Write("aaah");
            wr.Flush();

            fs.Close();
        }
    }
}
