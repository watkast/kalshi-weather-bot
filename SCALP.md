# Range-Scalp Bot

*Updated Sun Nov 08 03:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51898 | 45253 | 6645 (80) | 3 | $-14390.26 | -4.4% |
| **+10¢** | 38732 | 30980 | 7752 (106) | 2 | $-13419.06 | -5.5% |
| **+15¢** | 32436 | 24082 | 8354 (135) | 2 | $-12308.97 | -6.0% |
| **+20¢** | 28859 | 20102 | 8757 (180) | 2 | $-10826.98 | -6.0% |
| **+10¢ (15¢ stop)** | 63205 | 63102 | 103 (61) | 0 | $-23414.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 03:22 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-08 03:19 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.69 |
| 11-08 03:19 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-08 03:19 | +5 | XRP | UP | 0.58 | open |  |
| 11-08 03:19 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 11-08 03:18 | +10 stop | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 11-08 03:18 | +20 | BTC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-08 03:18 | +15 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 11-08 03:18 | +10 | BTC | DOWN | 0.56 | 0.69 | 0.97 |
| 11-08 03:18 | +5 | BTC | DOWN | 0.57 | 0.64 | 0.35 |
| 11-08 03:17 | +10 stop | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 11-08 03:17 | +20 | ETH | DOWN | 0.60 | 0.84 | 2.13 |
| 11-08 03:17 | +15 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 11-08 03:17 | +10 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 11-08 03:17 | +5 | ETH | DOWN | 0.60 | 0.75 | 1.19 |
| 11-08 03:17 | +10 stop | SOL | UP | 0.54 | 0.39 | -1.85 |
| 11-08 03:17 | +10 stop | XRP | UP | 0.55 | 0.34 | -2.39 |
| 11-08 03:17 | +20 | XRP | UP | 0.55 | open |  |
| 11-08 03:17 | +15 | XRP | UP | 0.54 | open |  |
| 11-08 03:17 | +10 | XRP | UP | 0.55 | open |  |
| 11-08 03:17 | +5 | XRP | UP | 0.55 | 0.60 | 0.15 |
| 11-08 03:17 | +10 stop | BNB | UP | 0.58 | 0.38 | -2.35 |
| 11-08 03:17 | +20 | BNB | UP | 0.58 | open |  |
| 11-08 03:17 | +15 | BNB | UP | 0.58 | open |  |
| 11-08 03:17 | +10 | BNB | UP | 0.58 | open |  |
| 11-08 03:17 | +5 | BNB | UP | 0.58 | open |  |
| 11-08 03:17 | +5 | SOL | UP | 0.58 | open |  |
| 11-08 03:16 | +10 stop | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 03:16 | +20 | DOGE | DOWN | 0.63 | 0.87 | 2.15 |
| 11-08 03:16 | +15 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 03:16 | +10 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 03:16 | +5 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 03:16 | +10 stop | SOL | DOWN | 0.56 | 0.41 | -1.85 |
| 11-08 03:16 | +20 | SOL | DOWN | 0.56 | 0.81 | 2.21 |
| 11-08 03:16 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 11-08 03:16 | +10 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 11-08 03:16 | +5 | SOL | DOWN | 0.53 | 0.60 | 0.35 |
| 11-08 03:16 | +10 stop | NEAR | DOWN | 0.63 | 0.77 | 1.10 |
| 11-08 03:16 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-08 03:16 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
