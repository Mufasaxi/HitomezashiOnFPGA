module HitomezashiEffect (
  input wire signed [15:0] i_x,
  input wire signed [15:0] i_y,
  input wire pix_clk,
  input wire framestart,
  output reg [7:0] o_red,
  output reg [7:0] o_green,
  output reg [7:0] o_blue
);

  parameter WIDTH = 1280;                // Screen width
  parameter HEIGHT = 720;                // Screen height

  // Fixed bitstreams for rows and columns
  reg [7:0] row_bitstream = 8'b11001100;
  reg [7:0] col_bitstream = 8'b00110011;

  reg [3:0] row_index;
  reg [3:0] col_index;

  always @(posedge pix_clk) begin
    if (framestart) begin
      row_index <= 0;
      col_index <= 0;
    end else begin
      if (i_x[3:0] == 0 && i_y[3:0] == 0) begin
        if (row_index == 7)
          row_index <= 0;
        else
          row_index <= row_index + 1;

        if (col_index == 7)
          col_index <= 0;
        else
          col_index <= col_index + 1;
      end
    end

    // Calculate the current row and column values using bit shifting
    reg [7:0] row_value = row_bitstream << row_index;
    reg [7:0] col_value = col_bitstream << col_index;

    // Set the RGB output values based on the hitomezashi effect
    o_red <= row_value & col_value;
    o_green <= 0;
    o_blue <= 0;
  end
endmodule