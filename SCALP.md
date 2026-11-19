# Range-Scalp Bot

*Updated Thu Nov 19 14:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65033 | 56761 | 8272 (124) | 4 | $-17467.41 | -4.3% |
| **+10¢** | 48579 | 38903 | 9676 (165) | 4 | $-16244.86 | -5.3% |
| **+15¢** | 40736 | 30299 | 10437 (210) | 4 | $-14659.57 | -5.7% |
| **+20¢** | 36278 | 25317 | 10961 (265) | 4 | $-12953.41 | -5.7% |
| **+10¢ (15¢ stop)** | 79157 | 78993 | 164 (98) | 0 | $-29078.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 14:26 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 11-19 14:23 | +10 stop | XRP | DOWN | 0.66 | 0.50 | -1.94 |
| 11-19 14:23 | +10 stop | NEAR | DOWN | 0.60 | 0.45 | -1.89 |
| 11-19 14:23 | +10 stop | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 11-19 14:22 | +10 stop | SOL | DOWN | 0.59 | 0.42 | -2.05 |
| 11-19 14:22 | +5 | NEAR | UP | 0.67 | open |  |
| 11-19 14:21 | +5 | BNB | DOWN | 0.56 | 0.71 | 1.17 |
| 11-19 14:21 | +10 stop | DOGE | DOWN | 0.56 | 0.72 | 1.27 |
| 11-19 14:21 | +10 | DOGE | DOWN | 0.59 | 0.72 | 0.98 |
| 11-19 14:20 | +5 | DOGE | DOWN | 0.63 | 0.72 | 0.58 |
| 11-19 14:20 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-19 14:20 | +5 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-19 14:20 | +10 stop | NEAR | UP | 0.66 | 0.41 | -2.83 |
| 11-19 14:20 | +20 | NEAR | UP | 0.64 | open |  |
| 11-19 14:20 | +10 | NEAR | UP | 0.65 | open |  |
| 11-19 14:20 | +5 | NEAR | UP | 0.60 | 0.72 | 0.88 |
| 11-19 14:20 | +10 stop | ZEC | UP | 0.54 | 0.36 | -2.15 |
| 11-19 14:20 | +15 | ZEC | UP | 0.54 | open |  |
| 11-19 14:20 | +10 | ZEC | UP | 0.56 | open |  |
| 11-19 14:19 | +10 stop | HYPE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-19 14:19 | +10 stop | BNB | DOWN | 0.62 | 0.79 | 1.41 |
| 11-19 14:19 | +5 | SOL | UP | 0.64 | open |  |
| 11-19 14:19 | +10 stop | SOL | UP | 0.57 | 0.41 | -1.95 |
| 11-19 14:19 | +20 | SOL | UP | 0.57 | open |  |
| 11-19 14:19 | +15 | SOL | UP | 0.57 | open |  |
| 11-19 14:19 | +10 | SOL | UP | 0.56 | open |  |
| 11-19 14:19 | +5 | SOL | UP | 0.56 | 0.65 | 0.56 |
| 11-19 14:19 | +10 stop | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-19 14:19 | +15 | NEAR | UP | 0.64 | open |  |
| 11-19 14:19 | +10 | NEAR | UP | 0.64 | 0.76 | 0.90 |
| 11-19 14:19 | +5 | NEAR | UP | 0.64 | 0.70 | 0.28 |
| 11-19 14:19 | +10 | XRP | UP | 0.60 | 0.74 | 1.09 |
| 11-19 14:18 | +10 stop | BNB | UP | 0.54 | 0.33 | -2.44 |
| 11-19 14:18 | +5 | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-19 14:18 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 11-19 14:17 | +5 | ZEC | UP | 0.71 | open |  |
| 11-19 14:17 | +10 stop | DOGE | DOWN | 0.52 | 0.62 | 0.65 |
| 11-19 14:17 | +20 | DOGE | DOWN | 0.52 | 0.72 | 1.67 |
| 11-19 14:17 | +15 | DOGE | DOWN | 0.52 | 0.72 | 1.67 |
| 11-19 14:17 | +10 | DOGE | DOWN | 0.52 | 0.62 | 0.65 |
