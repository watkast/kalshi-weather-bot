# Range-Scalp Bot

*Updated Sat Oct 31 20:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42667 | 37200 | 5467 (61) | 0 | $-12089.30 | -4.5% |
| **+10¢** | 31819 | 25494 | 6325 (83) | 1 | $-10865.59 | -5.4% |
| **+15¢** | 26617 | 19795 | 6822 (111) | 1 | $-9981.07 | -6.0% |
| **+20¢** | 23641 | 16492 | 7149 (143) | 1 | $-8853.76 | -6.0% |
| **+10¢ (15¢ stop)** | 52061 | 51978 | 83 (48) | 1 | $-19702.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 20:08 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 10-31 20:04 | +10 stop | HYPE | UP | 0.67 | open |  |
| 10-31 20:04 | +20 | HYPE | UP | 0.67 | open |  |
| 10-31 20:04 | +15 | HYPE | UP | 0.68 | open |  |
| 10-31 20:04 | +10 | HYPE | UP | 0.66 | open |  |
| 10-31 20:04 | +5 | HYPE | UP | 0.66 | 0.72 | 0.25 |
| 10-31 20:01 | +10 stop | BNB | UP | 0.65 | 0.83 | 1.54 |
| 10-31 20:01 | +20 | BNB | UP | 0.65 | 0.87 | 1.96 |
| 10-31 20:01 | +15 | BNB | UP | 0.65 | 0.83 | 1.54 |
| 10-31 20:01 | +10 | BNB | UP | 0.65 | 0.83 | 1.54 |
| 10-31 20:01 | +5 | BNB | UP | 0.65 | 0.83 | 1.54 |
| 10-31 20:00 | +10 stop | BTC | UP | 0.70 | 0.84 | 1.15 |
| 10-31 20:00 | +20 | BTC | UP | 0.70 | 0.92 | 1.96 |
| 10-31 20:00 | +15 | BTC | UP | 0.70 | 0.87 | 1.47 |
| 10-31 20:00 | +10 | BTC | UP | 0.69 | 0.84 | 1.25 |
| 10-31 20:00 | +5 | BTC | UP | 0.69 | 0.75 | 0.31 |
| 10-31 20:00 | +10 stop | XRP | UP | 0.63 | 0.80 | 1.41 |
| 10-31 20:00 | +20 | XRP | UP | 0.63 | 0.86 | 2.04 |
| 10-31 20:00 | +15 | XRP | UP | 0.63 | 0.80 | 1.41 |
| 10-31 20:00 | +10 | XRP | UP | 0.63 | 0.80 | 1.41 |
| 10-31 20:00 | +5 | XRP | UP | 0.63 | 0.72 | 0.58 |
| 10-31 19:55 | +10 stop | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 10-31 19:54 | +10 stop | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 19:54 | +20 | HYPE | DOWN | 0.63 | 0.86 | 2.04 |
| 10-31 19:54 | +15 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 19:54 | +10 | HYPE | DOWN | 0.63 | 0.78 | 1.20 |
| 10-31 19:54 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-31 19:53 | +10 stop | NEAR | UP | 0.59 | 0.34 | -2.87 |
| 10-31 19:53 | +5 | NEAR | UP | 0.62 | no | -6.42 |
| 10-31 19:52 | +10 stop | NEAR | DOWN | 0.57 | 0.41 | -1.95 |
| 10-31 19:52 | +20 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 19:52 | +15 | NEAR | DOWN | 0.57 | 0.78 | 1.79 |
| 10-31 19:52 | +10 | NEAR | DOWN | 0.57 | 0.67 | 0.66 |
| 10-31 19:52 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-31 19:42 | +10 stop | BNB | UP | 0.71 | 0.90 | 1.69 |
| 10-31 19:41 | +10 | SOL | DOWN | 0.69 | 1.00 | 2.90 |
| 10-31 19:41 | +5 | SOL | DOWN | 0.69 | 1.00 | 2.90 |
| 10-31 19:41 | +10 stop | SOL | DOWN | 0.70 | 0.30 | -4.30 |
| 10-31 19:41 | +15 | SOL | DOWN | 0.70 | 1.00 | 2.80 |
| 10-31 19:38 | +10 stop | HYPE | UP | 0.66 | 0.86 | 1.71 |
