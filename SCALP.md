# Range-Scalp Bot

*Updated Sun Nov 22 19:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68987 | 60204 | 8783 (145) | 6 | $-18509.69 | -4.3% |
| **+10¢** | 51476 | 41219 | 10257 (188) | 6 | $-17156.38 | -5.3% |
| **+15¢** | 43139 | 32079 | 11060 (240) | 8 | $-15415.98 | -5.7% |
| **+20¢** | 38410 | 26788 | 11622 (299) | 8 | $-13713.59 | -5.7% |
| **+10¢ (15¢ stop)** | 83986 | 83797 | 189 (117) | 6 | $-30928.60 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 19:06 | +5 | NEAR | UP | 0.56 | open |  |
| 11-22 19:06 | +10 stop | NEAR | UP | 0.60 | open |  |
| 11-22 19:05 | +5 | ETH | UP | 0.67 | 0.78 | 0.81 |
| 11-22 19:05 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 11-22 19:04 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 11-22 19:03 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 11-22 19:03 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 19:03 | +10 | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-22 19:03 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.63 |
| 11-22 19:03 | +10 stop | DOGE | UP | 0.64 | open |  |
| 11-22 19:03 | +5 | DOGE | UP | 0.64 | open |  |
| 11-22 19:03 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 11-22 19:03 | +10 stop | SOL | UP | 0.67 | 0.48 | -2.24 |
| 11-22 19:03 | +10 stop | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 19:03 | +20 | BNB | DOWN | 0.71 | open |  |
| 11-22 19:03 | +15 | BNB | DOWN | 0.71 | open |  |
| 11-22 19:03 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-22 19:03 | +5 | BNB | DOWN | 0.71 | 0.79 | 0.53 |
| 11-22 19:03 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.72 |
| 11-22 19:03 | +20 | ETH | UP | 0.68 | open |  |
| 11-22 19:03 | +15 | ETH | UP | 0.68 | open |  |
| 11-22 19:03 | +10 | ETH | UP | 0.68 | 0.78 | 0.72 |
| 11-22 19:03 | +5 | ETH | UP | 0.68 | 0.73 | 0.21 |
| 11-22 19:03 | +10 stop | NEAR | UP | 0.60 | 0.44 | -1.94 |
| 11-22 19:03 | +20 | NEAR | UP | 0.60 | open |  |
| 11-22 19:03 | +15 | NEAR | UP | 0.60 | open |  |
| 11-22 19:03 | +10 | NEAR | UP | 0.60 | open |  |
| 11-22 19:03 | +5 | NEAR | UP | 0.60 | 0.65 | 0.18 |
| 11-22 19:02 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-22 19:01 | +10 stop | SOL | DOWN | 0.70 | 0.33 | -4.01 |
| 11-22 19:01 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-22 19:01 | +15 | SOL | DOWN | 0.70 | open |  |
| 11-22 19:01 | +10 | SOL | DOWN | 0.70 | open |  |
| 11-22 19:01 | +5 | SOL | DOWN | 0.70 | open |  |
| 11-22 19:01 | +10 stop | ZEC | DOWN | 0.70 | 0.48 | -2.53 |
| 11-22 19:01 | +20 | ZEC | DOWN | 0.70 | open |  |
| 11-22 19:01 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-22 19:01 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-22 19:01 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-22 19:01 | +10 stop | XRP | DOWN | 0.63 | 0.39 | -2.74 |
