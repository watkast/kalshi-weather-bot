# Range-Scalp Bot

*Updated Tue Oct 27 21:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37090 | 32386 | 4704 (45) | 7 | $-10280.05 | -4.4% |
| **+10¢** | 27702 | 22252 | 5450 (67) | 8 | $-9159.92 | -5.3% |
| **+15¢** | 23175 | 17322 | 5853 (91) | 7 | $-8121.73 | -5.6% |
| **+20¢** | 20533 | 14409 | 6124 (116) | 8 | $-7083.43 | -5.5% |
| **+10¢ (15¢ stop)** | 45444 | 45379 | 65 (34) | 1 | $-17310.67 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 21:20 | +10 stop | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-27 21:19 | +10 stop | XRP | DOWN | 0.62 | 0.45 | -2.03 |
| 10-27 21:19 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-27 21:19 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 10-27 21:19 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 10-27 21:19 | +10 | BTC | DOWN | 0.68 | open |  |
| 10-27 21:19 | +5 | BTC | DOWN | 0.68 | open |  |
| 10-27 21:18 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-27 21:18 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-27 21:18 | +10 stop | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 10-27 21:18 | +20 | BTC | DOWN | 0.56 | open |  |
| 10-27 21:18 | +15 | BTC | DOWN | 0.56 | 0.71 | 1.17 |
| 10-27 21:18 | +10 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 10-27 21:18 | +5 | BTC | DOWN | 0.56 | 0.67 | 0.76 |
| 10-27 21:18 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-27 21:17 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 10-27 21:17 | +10 stop | ETH | UP | 0.54 | 0.35 | -2.24 |
| 10-27 21:17 | +10 stop | HYPE | DOWN | 0.60 | 0.75 | 1.15 |
| 10-27 21:17 | +10 stop | BNB | DOWN | 0.53 | 0.64 | 0.75 |
| 10-27 21:17 | +20 | BNB | DOWN | 0.53 | 0.74 | 1.78 |
| 10-27 21:17 | +15 | BNB | DOWN | 0.53 | 0.68 | 1.16 |
| 10-27 21:17 | +10 | BNB | DOWN | 0.53 | 0.64 | 0.75 |
| 10-27 21:17 | +5 | BNB | DOWN | 0.53 | 0.60 | 0.35 |
| 10-27 21:17 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 10-27 21:16 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.96 |
| 10-27 21:16 | +20 | XRP | UP | 0.58 | open |  |
| 10-27 21:16 | +15 | XRP | UP | 0.58 | open |  |
| 10-27 21:16 | +10 | XRP | UP | 0.58 | open |  |
| 10-27 21:16 | +5 | XRP | UP | 0.58 | open |  |
| 10-27 21:16 | +10 stop | DOGE | UP | 0.59 | 0.36 | -2.64 |
| 10-27 21:16 | +20 | DOGE | UP | 0.59 | open |  |
| 10-27 21:16 | +15 | DOGE | UP | 0.59 | open |  |
| 10-27 21:16 | +10 | DOGE | UP | 0.59 | open |  |
| 10-27 21:16 | +5 | DOGE | UP | 0.59 | 0.64 | 0.16 |
| 10-27 21:16 | +10 stop | SOL | UP | 0.63 | 0.47 | -1.95 |
| 10-27 21:16 | +20 | SOL | UP | 0.63 | open |  |
| 10-27 21:16 | +15 | SOL | UP | 0.63 | open |  |
| 10-27 21:16 | +10 | SOL | UP | 0.63 | open |  |
| 10-27 21:16 | +5 | SOL | UP | 0.63 | open |  |
| 10-27 21:16 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
