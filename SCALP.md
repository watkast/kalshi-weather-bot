# Range-Scalp Bot

*Updated Tue Oct 27 06:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36095 | 31510 | 4585 (43) | 3 | $-10043.63 | -4.4% |
| **+10¢** | 26982 | 21678 | 5304 (65) | 2 | $-8881.24 | -5.2% |
| **+15¢** | 22581 | 16883 | 5698 (89) | 2 | $-7867.47 | -5.5% |
| **+20¢** | 20017 | 14047 | 5970 (112) | 2 | $-6905.59 | -5.5% |
| **+10¢ (15¢ stop)** | 44264 | 44201 | 63 (33) | 2 | $-16867.47 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 06:16 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-27 06:16 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 10-27 06:16 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-27 06:16 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-27 06:16 | +10 | DOGE | DOWN | 0.64 | open |  |
| 10-27 06:16 | +5 | DOGE | DOWN | 0.64 | open |  |
| 10-27 06:16 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 10-27 06:16 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-27 06:16 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-27 06:16 | +10 | XRP | DOWN | 0.64 | open |  |
| 10-27 06:16 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-27 06:12 | +10 stop | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-27 06:12 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-27 06:11 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 06:11 | +20 | ZEC | DOWN | 0.71 | 0.95 | 2.22 |
| 10-27 06:11 | +15 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 10-27 06:11 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 06:11 | +5 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 06:10 | +10 stop | XRP | UP | 0.71 | 0.36 | -3.82 |
| 10-27 06:10 | +10 | XRP | UP | 0.71 | no | -7.25 |
| 10-27 06:10 | +5 | XRP | UP | 0.71 | no | -7.25 |
| 10-27 06:10 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-27 06:10 | +20 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-27 06:10 | +15 | BNB | DOWN | 0.64 | 0.85 | 1.84 |
| 10-27 06:10 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 10-27 06:10 | +5 | BNB | DOWN | 0.64 | 0.71 | 0.38 |
| 10-27 06:10 | +10 stop | XRP | DOWN | 0.44 | 0.56 | 0.84 |
| 10-27 06:10 | +20 | XRP | DOWN | 0.44 | 0.64 | 1.65 |
| 10-27 06:10 | +15 | XRP | DOWN | 0.44 | 0.61 | 1.35 |
| 10-27 06:10 | +10 | XRP | DOWN | 0.44 | 0.56 | 0.84 |
| 10-27 06:10 | +5 | XRP | DOWN | 0.44 | 0.56 | 0.84 |
| 10-27 06:09 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 06:09 | +20 | DOGE | DOWN | 0.71 | 0.93 | 1.96 |
| 10-27 06:09 | +15 | DOGE | DOWN | 0.71 | 0.88 | 1.47 |
| 10-27 06:09 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 06:09 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 10-27 05:47 | +5 | SOL | UP | 0.71 | 0.77 | 0.32 |
| 10-27 05:47 | +10 stop | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-27 05:47 | +20 | ETH | UP | 0.69 | 0.93 | 2.22 |
| 10-27 05:47 | +15 | ETH | UP | 0.69 | 0.84 | 1.25 |
