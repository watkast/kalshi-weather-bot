# Range-Scalp Bot

*Updated Tue Nov 10 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54174 | 47261 | 6913 (89) | 0 | $-14727.60 | -4.3% |
| **+10¢** | 40470 | 32402 | 8068 (117) | 0 | $-13684.97 | -5.4% |
| **+15¢** | 33918 | 25223 | 8695 (149) | 0 | $-12441.12 | -5.8% |
| **+20¢** | 30199 | 21081 | 9118 (195) | 1 | $-10847.42 | -5.7% |
| **+10¢ (15¢ stop)** | 66000 | 65890 | 110 (66) | 0 | $-24420.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 02:13 | +10 stop | NEAR | UP | 0.68 | 0.82 | 1.13 |
| 11-10 02:13 | +10 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 11-10 02:13 | +5 | NEAR | UP | 0.67 | 0.82 | 1.23 |
| 11-10 02:09 | +10 stop | NEAR | UP | 0.59 | 0.78 | 1.60 |
| 11-10 02:09 | +10 stop | DOGE | DOWN | 0.69 | 0.50 | -2.23 |
| 11-10 02:09 | +10 | DOGE | DOWN | 0.69 | 0.90 | 1.89 |
| 11-10 02:09 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-10 02:07 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-10 02:07 | +20 | DOGE | DOWN | 0.65 | 0.90 | 2.28 |
| 11-10 02:07 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-10 02:07 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 11-10 02:07 | +10 stop | NEAR | UP | 0.68 | 0.48 | -2.34 |
| 11-10 02:06 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-10 02:05 | +10 stop | DOGE | DOWN | 0.53 | 0.69 | 1.27 |
| 11-10 02:04 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-10 02:04 | +20 | BNB | DOWN | 0.65 | 0.88 | 2.06 |
| 11-10 02:04 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 11-10 02:04 | +10 | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-10 02:04 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 11-10 02:04 | +15 | NEAR | UP | 0.70 | 0.95 | 2.32 |
| 11-10 02:04 | +20 | NEAR | UP | 0.70 | 0.95 | 2.32 |
| 11-10 02:04 | +10 stop | DOGE | DOWN | 0.50 | 0.63 | 0.95 |
| 11-10 02:04 | +10 stop | ZEC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-10 02:04 | +15 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-10 02:04 | +10 | ZEC | DOWN | 0.69 | 0.81 | 0.94 |
| 11-10 02:04 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-10 02:03 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.97 |
| 11-10 02:03 | +5 | ETH | DOWN | 0.66 | 0.73 | 0.40 |
| 11-10 02:03 | +10 stop | NEAR | UP | 0.69 | 0.81 | 0.94 |
| 11-10 02:02 | +10 stop | DOGE | DOWN | 0.67 | 0.50 | -2.04 |
| 11-10 02:02 | +15 | DOGE | DOWN | 0.67 | 0.90 | 2.08 |
| 11-10 02:02 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-10 02:02 | +5 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-10 02:02 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 11-10 02:02 | +10 stop | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 02:02 | +20 | SOL | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 02:02 | +15 | SOL | DOWN | 0.70 | 0.90 | 1.78 |
| 11-10 02:02 | +10 | SOL | DOWN | 0.70 | 0.82 | 0.94 |
| 11-10 02:02 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-10 02:02 | +5 | ZEC | DOWN | 0.69 | 0.77 | 0.52 |
