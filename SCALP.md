# Range-Scalp Bot

*Updated Tue Oct 20 08:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25352 | 22080 | 3272 (31) | 1 | $-7374.13 | -4.6% |
| **+10¢** | 19080 | 15298 | 3782 (46) | 1 | $-6534.71 | -5.4% |
| **+15¢** | 15968 | 11894 | 4074 (70) | 1 | $-5875.49 | -5.9% |
| **+20¢** | 14114 | 9849 | 4265 (88) | 2 | $-5266.47 | -5.9% |
| **+10¢ (15¢ stop)** | 31109 | 31057 | 52 (30) | 0 | $-11520.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 08:08 | +5 | BNB | UP | 0.57 | 0.66 | 0.56 |
| 10-20 08:08 | +10 | BNB | UP | 0.61 | 0.87 | 2.35 |
| 10-20 08:08 | +5 | BNB | UP | 0.61 | 0.68 | 0.37 |
| 10-20 08:07 | +10 stop | BNB | UP | 0.70 | 0.87 | 1.47 |
| 10-20 08:07 | +10 stop | BNB | DOWN | 0.56 | 0.40 | -1.95 |
| 10-20 08:05 | +10 stop | BNB | DOWN | 0.55 | 0.67 | 0.89 |
| 10-20 08:03 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.72 |
| 10-20 08:03 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 08:03 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-20 08:03 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 10-20 08:03 | +5 | HYPE | DOWN | 0.63 | 0.77 | 1.10 |
| 10-20 08:02 | +10 stop | BNB | DOWN | 0.55 | 0.66 | 0.76 |
| 10-20 08:02 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-20 08:02 | +20 | ZEC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-20 08:02 | +15 | ZEC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-20 08:02 | +10 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-20 08:02 | +5 | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-20 08:01 | +10 stop | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-20 08:01 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 10-20 08:01 | +15 | ETH | DOWN | 0.69 | 0.87 | 1.57 |
| 10-20 08:01 | +10 | ETH | DOWN | 0.69 | 0.80 | 0.83 |
| 10-20 08:01 | +5 | ETH | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 08:01 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 08:01 | +20 | XRP | DOWN | 0.70 | 0.90 | 1.79 |
| 10-20 08:01 | +15 | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 10-20 08:01 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 08:01 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-20 08:01 | +10 stop | HYPE | DOWN | 0.70 | 0.51 | -2.23 |
| 10-20 08:01 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-20 08:01 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-20 08:01 | +10 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 10-20 08:01 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-20 08:01 | +10 stop | NEAR | UP | 0.49 | 0.20 | -3.20 |
| 10-20 08:01 | +20 | NEAR | UP | 0.49 | open |  |
| 10-20 08:01 | +15 | NEAR | UP | 0.49 | open |  |
| 10-20 08:01 | +10 | NEAR | UP | 0.49 | open |  |
| 10-20 08:01 | +5 | NEAR | UP | 0.49 | open |  |
| 10-20 08:01 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-20 08:01 | +20 | BTC | DOWN | 0.70 | 0.90 | 1.80 |
| 10-20 08:01 | +15 | BTC | DOWN | 0.70 | 0.86 | 1.36 |
