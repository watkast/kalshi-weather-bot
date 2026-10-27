# Range-Scalp Bot

*Updated Tue Oct 27 18:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36899 | 32222 | 4677 (44) | 2 | $-10215.67 | -4.4% |
| **+10¢** | 27563 | 22146 | 5417 (66) | 3 | $-9075.58 | -5.2% |
| **+15¢** | 23059 | 17245 | 5814 (90) | 6 | $-8004.95 | -5.5% |
| **+20¢** | 20437 | 14351 | 6086 (115) | 8 | $-6977.84 | -5.4% |
| **+10¢ (15¢ stop)** | 45198 | 45134 | 64 (33) | 3 | $-17212.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 18:19 | +5 | NEAR | UP | 0.66 | 0.76 | 0.71 |
| 10-27 18:18 | +10 stop | ETH | UP | 0.58 | open |  |
| 10-27 18:18 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-27 18:18 | +20 | SOL | UP | 0.67 | open |  |
| 10-27 18:18 | +15 | SOL | UP | 0.66 | open |  |
| 10-27 18:18 | +10 | SOL | UP | 0.67 | 0.80 | 1.02 |
| 10-27 18:18 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 10-27 18:18 | +10 stop | BTC | DOWN | 0.50 | open |  |
| 10-27 18:18 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-27 18:18 | +20 | DOGE | UP | 0.63 | 0.84 | 1.83 |
| 10-27 18:18 | +15 | DOGE | UP | 0.63 | 0.80 | 1.41 |
| 10-27 18:18 | +10 | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 10-27 18:18 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 10-27 18:17 | +10 stop | NEAR | UP | 0.61 | 0.76 | 1.20 |
| 10-27 18:17 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 10-27 18:17 | +20 | HYPE | UP | 0.69 | open |  |
| 10-27 18:17 | +15 | HYPE | UP | 0.69 | open |  |
| 10-27 18:17 | +10 | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 10-27 18:17 | +5 | HYPE | UP | 0.69 | 0.76 | 0.42 |
| 10-27 18:17 | +10 stop | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-27 18:17 | +20 | ZEC | UP | 0.68 | open |  |
| 10-27 18:17 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 10-27 18:17 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 10-27 18:17 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 10-27 18:16 | +10 stop | XRP | UP | 0.69 | 0.82 | 1.04 |
| 10-27 18:16 | +20 | XRP | UP | 0.69 | open |  |
| 10-27 18:16 | +15 | XRP | UP | 0.70 | open |  |
| 10-27 18:16 | +10 stop | ETH | UP | 0.67 | 0.52 | -1.84 |
| 10-27 18:16 | +20 | ETH | UP | 0.67 | open |  |
| 10-27 18:16 | +15 | ETH | UP | 0.67 | open |  |
| 10-27 18:16 | +10 | ETH | UP | 0.67 | open |  |
| 10-27 18:16 | +5 | ETH | UP | 0.67 | open |  |
| 10-27 18:16 | +10 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 10-27 18:16 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 10-27 18:15 | +10 stop | BNB | UP | 0.70 | open |  |
| 10-27 18:15 | +20 | BNB | UP | 0.70 | open |  |
| 10-27 18:15 | +15 | BNB | UP | 0.70 | open |  |
| 10-27 18:15 | +10 | BNB | UP | 0.70 | open |  |
| 10-27 18:15 | +5 | BNB | UP | 0.70 | 0.76 | 0.32 |
| 10-27 18:15 | +10 stop | BTC | UP | 0.67 | 0.49 | -2.14 |
