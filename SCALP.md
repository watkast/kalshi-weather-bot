# Range-Scalp Bot

*Updated Tue Oct 20 15:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25785 | 22460 | 3325 (31) | 0 | $-7502.21 | -4.6% |
| **+10¢** | 19415 | 15574 | 3841 (46) | 0 | $-6614.82 | -5.4% |
| **+15¢** | 16256 | 12120 | 4136 (70) | 0 | $-5906.96 | -5.8% |
| **+20¢** | 14381 | 10048 | 4333 (88) | 0 | $-5288.53 | -5.9% |
| **+10¢ (15¢ stop)** | 31628 | 31575 | 53 (30) | 0 | $-11645.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 15:06 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 10-20 15:06 | +20 | NEAR | DOWN | 0.69 | 0.89 | 1.79 |
| 10-20 15:06 | +15 | NEAR | DOWN | 0.69 | 0.88 | 1.68 |
| 10-20 15:06 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 10-20 15:06 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.53 |
| 10-20 15:02 | +10 stop | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 10-20 15:01 | +10 stop | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 15:01 | +20 | DOGE | DOWN | 0.68 | 0.91 | 2.02 |
| 10-20 15:01 | +15 | DOGE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-20 15:01 | +10 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 15:01 | +5 | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 15:01 | +10 stop | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 15:01 | +20 | SOL | DOWN | 0.66 | 0.86 | 1.75 |
| 10-20 15:01 | +15 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 15:01 | +10 | SOL | DOWN | 0.66 | 0.83 | 1.44 |
| 10-20 15:01 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 10-20 15:01 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 15:01 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.79 |
| 10-20 15:01 | +15 | BNB | DOWN | 0.70 | 0.89 | 1.68 |
| 10-20 15:01 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 15:01 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-20 15:01 | +10 stop | NEAR | DOWN | 0.69 | 0.51 | -2.13 |
| 10-20 15:01 | +20 | NEAR | DOWN | 0.69 | 0.91 | 1.97 |
| 10-20 15:01 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-20 15:01 | +10 | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 10-20 15:01 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 15:01 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 10-20 15:01 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-20 15:01 | +15 | ZEC | DOWN | 0.69 | 0.85 | 1.36 |
| 10-20 15:01 | +10 | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-20 15:01 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-20 15:01 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 15:01 | +20 | BTC | DOWN | 0.70 | 0.92 | 1.94 |
| 10-20 15:01 | +15 | BTC | DOWN | 0.70 | 0.92 | 1.94 |
| 10-20 15:01 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 15:01 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 10-20 14:57 | +20 | HYPE | DOWN | 0.53 | 0.84 | 2.82 |
| 10-20 14:57 | +15 | HYPE | DOWN | 0.54 | 0.84 | 2.72 |
| 10-20 14:57 | +10 | HYPE | DOWN | 0.54 | 0.84 | 2.72 |
| 10-20 14:57 | +5 | HYPE | DOWN | 0.51 | 0.59 | 0.45 |
