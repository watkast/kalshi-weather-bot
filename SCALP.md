# Range-Scalp Bot

*Updated Mon Oct 26 13:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34890 | 30465 | 4425 (43) | 2 | $-9646.53 | -4.4% |
| **+10¢** | 26112 | 20995 | 5117 (65) | 2 | $-8440.62 | -5.1% |
| **+15¢** | 21850 | 16340 | 5510 (89) | 3 | $-7549.41 | -5.5% |
| **+20¢** | 19365 | 13590 | 5775 (112) | 4 | $-6635.29 | -5.5% |
| **+10¢ (15¢ stop)** | 42688 | 42626 | 62 (33) | 1 | $-16180.19 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 13:38 | +10 stop | BNB | DOWN | 0.63 | 0.46 | -2.05 |
| 10-26 13:38 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-26 13:38 | +15 | BNB | DOWN | 0.65 | open |  |
| 10-26 13:38 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-26 13:38 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-26 13:38 | +10 stop | ETH | UP | 0.67 | open |  |
| 10-26 13:38 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-26 13:38 | +20 | SOL | UP | 0.64 | open |  |
| 10-26 13:38 | +15 | SOL | UP | 0.64 | open |  |
| 10-26 13:38 | +10 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-26 13:38 | +5 | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-26 13:37 | +10 stop | ETH | DOWN | 0.65 | 0.43 | -2.54 |
| 10-26 13:37 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-26 13:37 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-26 13:37 | +10 | ETH | DOWN | 0.64 | open |  |
| 10-26 13:37 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-26 13:36 | +10 stop | NEAR | DOWN | 0.56 | 0.28 | -3.13 |
| 10-26 13:34 | +10 stop | ZEC | UP | 0.50 | 0.29 | -2.43 |
| 10-26 13:34 | +10 stop | NEAR | UP | 0.57 | 0.37 | -2.35 |
| 10-26 13:33 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-26 13:33 | +20 | XRP | DOWN | 0.62 | 0.84 | 1.93 |
| 10-26 13:33 | +15 | XRP | DOWN | 0.62 | 0.77 | 1.20 |
| 10-26 13:33 | +10 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-26 13:33 | +5 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-26 13:33 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 10-26 13:33 | +5 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-26 13:32 | +10 stop | NEAR | DOWN | 0.62 | 0.37 | -2.84 |
| 10-26 13:32 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 10-26 13:32 | +5 | XRP | DOWN | 0.62 | 0.70 | 0.48 |
| 10-26 13:32 | +10 stop | ZEC | DOWN | 0.54 | 0.35 | -2.24 |
| 10-26 13:31 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-26 13:31 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.90 |
| 10-26 13:31 | +15 | BTC | DOWN | 0.71 | 0.92 | 1.90 |
| 10-26 13:31 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 13:31 | +5 | BTC | DOWN | 0.71 | 0.79 | 0.53 |
| 10-26 13:31 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-26 13:31 | +20 | ETH | DOWN | 0.71 | 0.93 | 2.00 |
| 10-26 13:31 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-26 13:31 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-26 13:31 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
