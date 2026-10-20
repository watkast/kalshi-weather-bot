# Range-Scalp Bot

*Updated Tue Oct 20 13:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 25711 | 22395 | 3316 (31) | 2 | $-7486.53 | -4.6% |
| **+10¢** | 19347 | 15517 | 3830 (46) | 2 | $-6607.51 | -5.4% |
| **+15¢** | 16197 | 12073 | 4124 (70) | 3 | $-5910.99 | -5.8% |
| **+20¢** | 14327 | 10010 | 4317 (88) | 4 | $-5266.53 | -5.9% |
| **+10¢ (15¢ stop)** | 31534 | 31481 | 53 (30) | 1 | $-11622.59 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-20 13:43 | +10 stop | SOL | DOWN | 0.64 | open |  |
| 10-20 13:42 | +10 stop | SOL | UP | 0.68 | 0.45 | -2.64 |
| 10-20 13:42 | +10 | SOL | UP | 0.66 | open |  |
| 10-20 13:42 | +5 | SOL | UP | 0.66 | open |  |
| 10-20 13:42 | +5 | BNB | DOWN | 0.60 | 0.76 | 1.28 |
| 10-20 13:41 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 13:41 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 10-20 13:41 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 10-20 13:38 | +10 stop | BNB | UP | 0.62 | 0.75 | 0.99 |
| 10-20 13:38 | +20 | BNB | UP | 0.62 | open |  |
| 10-20 13:38 | +15 | BNB | UP | 0.62 | open |  |
| 10-20 13:38 | +10 | BNB | UP | 0.61 | 0.75 | 1.09 |
| 10-20 13:38 | +5 | BNB | UP | 0.60 | 0.75 | 1.19 |
| 10-20 13:37 | +10 stop | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-20 13:37 | +20 | SOL | UP | 0.68 | open |  |
| 10-20 13:37 | +15 | SOL | UP | 0.68 | open |  |
| 10-20 13:37 | +10 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-20 13:37 | +5 | SOL | UP | 0.68 | 0.80 | 0.92 |
| 10-20 13:35 | +10 stop | BTC | DOWN | 0.56 | 0.38 | -2.15 |
| 10-20 13:35 | +5 | BTC | DOWN | 0.56 | 0.61 | 0.15 |
| 10-20 13:35 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-20 13:34 | +5 | XRP | DOWN | 0.51 | 0.66 | 1.16 |
| 10-20 13:33 | +10 stop | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 10-20 13:33 | +20 | NEAR | DOWN | 0.70 | open |  |
| 10-20 13:33 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 10-20 13:33 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 10-20 13:33 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 10-20 13:32 | +10 stop | BTC | DOWN | 0.68 | 0.52 | -1.94 |
| 10-20 13:32 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-20 13:32 | +10 stop | HYPE | DOWN | 0.65 | 0.82 | 1.39 |
| 10-20 13:31 | +10 stop | XRP | DOWN | 0.68 | 0.17 | -5.39 |
| 10-20 13:31 | +20 | XRP | DOWN | 0.68 | open |  |
| 10-20 13:31 | +15 | XRP | DOWN | 0.68 | open |  |
| 10-20 13:31 | +10 | XRP | DOWN | 0.68 | open |  |
| 10-20 13:31 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 10-20 13:31 | +5 | BTC | UP | 0.49 | 0.56 | 0.34 |
| 10-20 13:31 | +10 stop | HYPE | UP | 0.62 | 0.40 | -2.54 |
| 10-20 13:31 | +20 | HYPE | UP | 0.62 | 0.87 | 2.25 |
| 10-20 13:31 | +15 | HYPE | UP | 0.62 | 0.81 | 1.62 |
| 10-20 13:31 | +10 | HYPE | UP | 0.62 | 0.81 | 1.62 |
