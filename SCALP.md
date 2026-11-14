# Range-Scalp Bot

*Updated Sat Nov 14 20:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59838 | 52209 | 7629 (107) | 0 | $-16188.45 | -4.3% |
| **+10¢** | 44707 | 35773 | 8934 (143) | 1 | $-15223.38 | -5.4% |
| **+15¢** | 37454 | 27820 | 9634 (180) | 1 | $-13863.00 | -5.9% |
| **+20¢** | 33364 | 23255 | 10109 (232) | 2 | $-12212.29 | -5.8% |
| **+10¢ (15¢ stop)** | 72816 | 72673 | 143 (82) | 1 | $-26723.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 20:38 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-14 20:38 | +15 | BTC | DOWN | 0.68 | open |  |
| 11-14 20:38 | +10 | BTC | DOWN | 0.68 | open |  |
| 11-14 20:38 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-14 20:36 | +10 stop | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-14 20:36 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-14 20:36 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-14 20:36 | +5 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-14 20:32 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 20:32 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 20:32 | +5 | BTC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-14 20:31 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 20:31 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 20:31 | +20 | NEAR | DOWN | 0.70 | 0.92 | 1.94 |
| 11-14 20:31 | +15 | NEAR | DOWN | 0.70 | 0.85 | 1.26 |
| 11-14 20:31 | +10 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 20:31 | +5 | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-14 20:31 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-14 20:31 | +20 | BTC | DOWN | 0.61 | open |  |
| 11-14 20:31 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-14 20:31 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-14 20:31 | +5 | BTC | DOWN | 0.62 | 0.70 | 0.48 |
| 11-14 20:31 | +10 stop | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-14 20:31 | +20 | SOL | DOWN | 0.71 | 0.92 | 1.86 |
| 11-14 20:31 | +15 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-14 20:31 | +10 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-14 20:31 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-14 20:31 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 20:31 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-14 20:31 | +15 | BNB | DOWN | 0.68 | 0.83 | 1.24 |
| 11-14 20:31 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 20:31 | +10 stop | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 20:31 | +20 | XRP | DOWN | 0.71 | 0.93 | 2.01 |
| 11-14 20:31 | +15 | XRP | DOWN | 0.71 | 0.87 | 1.37 |
| 11-14 20:31 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 20:31 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 20:28 | +10 stop | SOL | UP | 0.25 | 0.59 | 3.09 |
| 11-14 20:28 | +10 | SOL | UP | 0.25 | 0.59 | 3.09 |
| 11-14 20:28 | +5 | SOL | UP | 0.25 | 0.59 | 3.09 |
| 11-14 20:27 | +10 stop | BTC | DOWN | 0.66 | 0.84 | 1.54 |
