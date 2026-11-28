# Range-Scalp Bot

*Updated Sat Nov 28 04:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74360 | 64908 | 9452 (171) | 4 | $-19728.16 | -4.2% |
| **+10¢** | 55394 | 44347 | 11047 (217) | 4 | $-18368.94 | -5.3% |
| **+15¢** | 46382 | 34488 | 11894 (275) | 5 | $-16400.64 | -5.6% |
| **+20¢** | 41273 | 28747 | 12526 (342) | 5 | $-14812.91 | -5.7% |
| **+10¢ (15¢ stop)** | 90491 | 90272 | 219 (135) | 3 | $-33429.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 04:16 | +10 stop | SOL | UP | 0.61 | open |  |
| 11-28 04:16 | +20 | SOL | UP | 0.61 | open |  |
| 11-28 04:16 | +15 | SOL | UP | 0.61 | open |  |
| 11-28 04:16 | +10 | SOL | UP | 0.61 | open |  |
| 11-28 04:16 | +5 | SOL | UP | 0.61 | open |  |
| 11-28 04:16 | +10 stop | BTC | UP | 0.55 | open |  |
| 11-28 04:16 | +20 | BTC | UP | 0.55 | open |  |
| 11-28 04:16 | +15 | BTC | UP | 0.55 | open |  |
| 11-28 04:16 | +10 | BTC | UP | 0.55 | open |  |
| 11-28 04:16 | +5 | BTC | UP | 0.55 | open |  |
| 11-28 04:16 | +10 stop | ETH | UP | 0.61 | open |  |
| 11-28 04:16 | +20 | ETH | UP | 0.61 | open |  |
| 11-28 04:16 | +15 | ETH | UP | 0.61 | open |  |
| 11-28 04:16 | +10 | ETH | UP | 0.61 | open |  |
| 11-28 04:16 | +5 | ETH | UP | 0.60 | open |  |
| 11-28 04:16 | +10 stop | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-28 04:16 | +20 | ZEC | DOWN | 0.38 | open |  |
| 11-28 04:16 | +15 | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-28 04:16 | +10 | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-28 04:16 | +5 | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-28 04:16 | +15 | NEAR | UP | 0.70 | open |  |
| 11-28 04:15 | +10 stop | HYPE | DOWN | 0.57 | 0.35 | -2.54 |
| 11-28 04:15 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-28 04:15 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-28 04:15 | +10 | HYPE | DOWN | 0.57 | open |  |
| 11-28 04:15 | +5 | HYPE | DOWN | 0.56 | open |  |
| 11-28 04:13 | +10 stop | NEAR | DOWN | 0.54 | 0.01 | -5.46 |
| 11-28 04:13 | +10 | NEAR | DOWN | 0.55 | yes | -5.68 |
| 11-28 04:13 | +5 | NEAR | DOWN | 0.55 | 0.62 | 0.35 |
| 11-28 04:11 | +5 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-28 04:10 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-28 04:10 | +10 stop | BNB | UP | 0.67 | 0.78 | 0.86 |
| 11-28 04:10 | +10 | BNB | UP | 0.67 | 0.78 | 0.86 |
| 11-28 04:10 | +5 | BNB | UP | 0.67 | 0.72 | 0.24 |
| 11-28 04:10 | +5 | BTC | UP | 0.58 | 0.64 | 0.25 |
| 11-28 04:09 | +10 stop | ETH | UP | 0.55 | 0.38 | -2.05 |
| 11-28 04:08 | +10 stop | XRP | DOWN | 0.53 | 0.63 | 0.65 |
| 11-28 04:07 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-28 04:07 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-28 04:07 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
