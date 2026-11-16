# Range-Scalp Bot

*Updated Mon Nov 16 23:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62412 | 54451 | 7961 (117) | 8 | $-16891.37 | -4.3% |
| **+10¢** | 46608 | 37291 | 9317 (159) | 8 | $-15776.79 | -5.4% |
| **+15¢** | 39056 | 29006 | 10050 (201) | 8 | $-14348.94 | -5.9% |
| **+20¢** | 34807 | 24266 | 10541 (256) | 8 | $-12551.35 | -5.7% |
| **+10¢ (15¢ stop)** | 75975 | 75819 | 156 (92) | 0 | $-28042.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 23:23 | +10 stop | HYPE | DOWN | 0.55 | 0.66 | 0.72 |
| 11-16 23:21 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-16 23:20 | +5 | HYPE | DOWN | 0.71 | open |  |
| 11-16 23:19 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 23:18 | +10 stop | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-16 23:18 | +20 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 11-16 23:18 | +15 | NEAR | DOWN | 0.60 | 0.82 | 1.92 |
| 11-16 23:18 | +10 | NEAR | DOWN | 0.60 | 0.70 | 0.68 |
| 11-16 23:18 | +5 | NEAR | DOWN | 0.60 | 0.66 | 0.27 |
| 11-16 23:18 | +10 stop | ETH | DOWN | 0.55 | 0.65 | 0.66 |
| 11-16 23:18 | +10 stop | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 11-16 23:18 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-16 23:18 | +10 stop | BNB | DOWN | 0.55 | 0.73 | 1.48 |
| 11-16 23:18 | +10 stop | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-16 23:17 | +10 stop | HYPE | DOWN | 0.68 | 0.50 | -2.14 |
| 11-16 23:17 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-16 23:17 | +15 | HYPE | DOWN | 0.68 | open |  |
| 11-16 23:17 | +10 | HYPE | DOWN | 0.68 | open |  |
| 11-16 23:17 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 23:17 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-16 23:17 | +10 stop | XRP | DOWN | 0.57 | 0.68 | 0.76 |
| 11-16 23:16 | +10 stop | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 23:16 | +5 | BTC | UP | 0.59 | open |  |
| 11-16 23:16 | +10 stop | ZEC | UP | 0.62 | 0.45 | -2.05 |
| 11-16 23:16 | +20 | ZEC | UP | 0.62 | open |  |
| 11-16 23:16 | +15 | ZEC | UP | 0.62 | open |  |
| 11-16 23:16 | +10 | ZEC | UP | 0.62 | open |  |
| 11-16 23:16 | +5 | ZEC | UP | 0.62 | open |  |
| 11-16 23:15 | +10 stop | DOGE | UP | 0.59 | 0.40 | -2.24 |
| 11-16 23:15 | +20 | DOGE | UP | 0.59 | open |  |
| 11-16 23:15 | +15 | DOGE | UP | 0.59 | open |  |
| 11-16 23:15 | +10 | DOGE | UP | 0.59 | open |  |
| 11-16 23:15 | +5 | DOGE | UP | 0.59 | open |  |
| 11-16 23:15 | +10 stop | XRP | UP | 0.62 | 0.40 | -2.54 |
| 11-16 23:15 | +20 | XRP | UP | 0.62 | open |  |
| 11-16 23:15 | +15 | XRP | UP | 0.62 | open |  |
| 11-16 23:15 | +10 | XRP | UP | 0.62 | open |  |
| 11-16 23:15 | +5 | XRP | UP | 0.62 | open |  |
| 11-16 23:15 | +10 stop | BTC | UP | 0.59 | 0.43 | -1.95 |
| 11-16 23:15 | +20 | BTC | UP | 0.59 | open |  |
