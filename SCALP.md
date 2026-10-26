# Range-Scalp Bot

*Updated Mon Oct 26 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 34111 | 29782 | 4329 (43) | 3 | $-9424.66 | -4.4% |
| **+10¢** | 25528 | 20521 | 5007 (65) | 5 | $-8278.26 | -5.2% |
| **+15¢** | 21346 | 15956 | 5390 (89) | 5 | $-7402.40 | -5.5% |
| **+20¢** | 18917 | 13272 | 5645 (111) | 5 | $-6492.80 | -5.5% |
| **+10¢ (15¢ stop)** | 41787 | 41725 | 62 (33) | 0 | $-15936.91 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 02:13 | +10 stop | ETH | UP | 0.59 | 0.34 | -2.83 |
| 10-26 02:13 | +5 | ETH | UP | 0.56 | 0.63 | 0.33 |
| 10-26 02:12 | +10 stop | ETH | DOWN | 0.55 | 0.21 | -3.70 |
| 10-26 02:12 | +10 | ETH | DOWN | 0.56 | open |  |
| 10-26 02:12 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.36 |
| 10-26 02:11 | +10 stop | DOGE | UP | 0.70 | 0.83 | 1.05 |
| 10-26 02:11 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-26 02:10 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 10-26 02:10 | +20 | ETH | DOWN | 0.57 | open |  |
| 10-26 02:10 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-26 02:10 | +10 | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 02:10 | +5 | ETH | DOWN | 0.57 | 0.71 | 1.07 |
| 10-26 02:10 | +10 stop | XRP | UP | 0.59 | 0.37 | -2.54 |
| 10-26 02:10 | +20 | XRP | UP | 0.59 | 0.85 | 2.34 |
| 10-26 02:10 | +15 | XRP | UP | 0.59 | 0.85 | 2.34 |
| 10-26 02:10 | +10 | XRP | UP | 0.59 | 0.85 | 2.34 |
| 10-26 02:10 | +5 | XRP | UP | 0.59 | 0.65 | 0.27 |
| 10-26 02:10 | +10 stop | NEAR | UP | 0.56 | 0.36 | -2.35 |
| 10-26 02:09 | +10 stop | HYPE | UP | 0.64 | 0.44 | -2.35 |
| 10-26 02:05 | +5 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 10-26 02:04 | +10 stop | HYPE | UP | 0.68 | 0.82 | 1.13 |
| 10-26 02:04 | +10 stop | BTC | UP | 0.68 | 0.78 | 0.71 |
| 10-26 02:04 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-26 02:03 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.86 |
| 10-26 02:03 | +10 stop | DOGE | UP | 0.66 | 0.82 | 1.33 |
| 10-26 02:03 | +5 | XRP | UP | 0.68 | 0.82 | 1.13 |
| 10-26 02:03 | +10 stop | BTC | UP | 0.54 | 0.65 | 0.76 |
| 10-26 02:03 | +5 | ETH | UP | 0.66 | 0.73 | 0.40 |
| 10-26 02:03 | +10 stop | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 10-26 02:03 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.72 |
| 10-26 02:02 | +10 stop | ETH | UP | 0.59 | 0.73 | 1.09 |
| 10-26 02:02 | +20 | ETH | UP | 0.59 | 0.82 | 2.02 |
| 10-26 02:02 | +15 | ETH | UP | 0.58 | 0.73 | 1.18 |
| 10-26 02:02 | +10 | ETH | UP | 0.58 | 0.73 | 1.18 |
| 10-26 02:02 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 10-26 02:02 | +5 | BNB | UP | 0.58 | 0.65 | 0.36 |
| 10-26 02:02 | +10 stop | XRP | UP | 0.61 | 0.82 | 1.82 |
| 10-26 02:02 | +20 | XRP | UP | 0.60 | 0.82 | 1.92 |
| 10-26 02:02 | +15 | XRP | UP | 0.60 | 0.82 | 1.92 |
| 10-26 02:02 | +10 | XRP | UP | 0.60 | 0.82 | 1.92 |
