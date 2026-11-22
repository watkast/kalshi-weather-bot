# Range-Scalp Bot

*Updated Sun Nov 22 22:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69170 | 60354 | 8816 (145) | 3 | $-18627.96 | -4.3% |
| **+10¢** | 51619 | 41326 | 10293 (188) | 3 | $-17274.47 | -5.3% |
| **+15¢** | 43261 | 32167 | 11094 (241) | 4 | $-15478.60 | -5.7% |
| **+20¢** | 38526 | 26867 | 11659 (300) | 5 | $-13766.20 | -5.7% |
| **+10¢ (15¢ stop)** | 84242 | 84053 | 189 (117) | 1 | $-31043.82 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 22:20 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 11-22 22:20 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-22 22:20 | +10 stop | BNB | DOWN | 0.62 | 0.72 | 0.68 |
| 11-22 22:18 | +10 stop | BNB | DOWN | 0.59 | 0.70 | 0.79 |
| 11-22 22:18 | +5 | XRP | DOWN | 0.67 | 0.79 | 0.92 |
| 11-22 22:18 | +5 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-22 22:18 | +10 stop | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 22:18 | +10 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 22:18 | +5 | DOGE | DOWN | 0.59 | 0.73 | 1.09 |
| 11-22 22:18 | +10 stop | DOGE | UP | 0.46 | 0.59 | 0.95 |
| 11-22 22:18 | +20 | DOGE | UP | 0.47 | open |  |
| 11-22 22:18 | +15 | DOGE | UP | 0.47 | open |  |
| 11-22 22:18 | +10 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-22 22:18 | +5 | DOGE | UP | 0.47 | 0.59 | 0.85 |
| 11-22 22:17 | +5 | BTC | UP | 0.60 | open |  |
| 11-22 22:17 | +10 stop | BNB | UP | 0.63 | 0.40 | -2.64 |
| 11-22 22:17 | +20 | BNB | UP | 0.63 | open |  |
| 11-22 22:17 | +15 | BNB | UP | 0.63 | open |  |
| 11-22 22:17 | +10 | BNB | UP | 0.63 | open |  |
| 11-22 22:17 | +5 | BNB | UP | 0.63 | open |  |
| 11-22 22:17 | +5 | SOL | DOWN | 0.53 | 0.60 | 0.35 |
| 11-22 22:17 | +10 stop | ETH | UP | 0.68 | 0.37 | -3.43 |
| 11-22 22:17 | +20 | ETH | UP | 0.68 | open |  |
| 11-22 22:17 | +15 | ETH | UP | 0.68 | open |  |
| 11-22 22:17 | +10 | ETH | UP | 0.67 | open |  |
| 11-22 22:17 | +5 | ETH | UP | 0.65 | open |  |
| 11-22 22:16 | +10 stop | BTC | UP | 0.55 | 0.39 | -1.95 |
| 11-22 22:16 | +20 | BTC | UP | 0.54 | open |  |
| 11-22 22:16 | +15 | BTC | UP | 0.54 | open |  |
| 11-22 22:16 | +10 | BTC | UP | 0.54 | open |  |
| 11-22 22:16 | +5 | BTC | UP | 0.54 | 0.59 | 0.15 |
| 11-22 22:16 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-22 22:16 | +20 | ZEC | DOWN | 0.67 | 0.88 | 1.86 |
| 11-22 22:16 | +15 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-22 22:16 | +10 | ZEC | DOWN | 0.66 | 0.79 | 1.00 |
| 11-22 22:16 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 11-22 22:16 | +10 stop | SOL | DOWN | 0.55 | 0.68 | 0.96 |
| 11-22 22:16 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-22 22:16 | +15 | SOL | DOWN | 0.58 | 0.74 | 1.28 |
| 11-22 22:16 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
