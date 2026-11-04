# Range-Scalp Bot

*Updated Wed Nov 04 19:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47453 | 41318 | 6135 (73) | 3 | $-13689.24 | -4.6% |
| **+10¢** | 35450 | 28333 | 7117 (98) | 3 | $-12522.52 | -5.6% |
| **+15¢** | 29689 | 22026 | 7663 (126) | 3 | $-11483.10 | -6.2% |
| **+20¢** | 26380 | 18354 | 8026 (166) | 3 | $-10137.99 | -6.1% |
| **+10¢ (15¢ stop)** | 57843 | 57750 | 93 (56) | 0 | $-21556.67 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 19:34 | +10 stop | DOGE | DOWN | 0.71 | 0.84 | 1.05 |
| 11-04 19:33 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.81 |
| 11-04 19:32 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-04 19:32 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-04 19:32 | +15 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 11-04 19:32 | +10 | BTC | DOWN | 0.60 | 0.74 | 1.09 |
| 11-04 19:32 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-04 19:32 | +10 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-04 19:32 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-04 19:32 | +10 stop | BNB | DOWN | 0.57 | 0.69 | 0.87 |
| 11-04 19:32 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 19:32 | +20 | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 11-04 19:32 | +15 | NEAR | DOWN | 0.63 | 0.81 | 1.52 |
| 11-04 19:32 | +10 | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 19:32 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-04 19:32 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-04 19:32 | +20 | SOL | DOWN | 0.55 | 0.75 | 1.68 |
| 11-04 19:32 | +15 | SOL | DOWN | 0.55 | 0.74 | 1.58 |
| 11-04 19:32 | +10 | SOL | DOWN | 0.55 | 0.66 | 0.76 |
| 11-04 19:32 | +5 | SOL | DOWN | 0.55 | 0.66 | 0.76 |
| 11-04 19:31 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 19:31 | +20 | ZEC | DOWN | 0.64 | 0.86 | 1.94 |
| 11-04 19:31 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-04 19:31 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-04 19:31 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-04 19:31 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 19:31 | +20 | ETH | DOWN | 0.58 | 0.80 | 1.90 |
| 11-04 19:31 | +15 | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 19:31 | +10 | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-04 19:31 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-04 19:31 | +10 stop | XRP | UP | 0.69 | 0.53 | -1.93 |
| 11-04 19:31 | +20 | XRP | UP | 0.69 | open |  |
| 11-04 19:31 | +15 | XRP | UP | 0.69 | open |  |
| 11-04 19:31 | +10 | XRP | UP | 0.69 | open |  |
| 11-04 19:31 | +5 | XRP | UP | 0.69 | open |  |
| 11-04 19:31 | +10 stop | BNB | UP | 0.59 | 0.41 | -2.14 |
| 11-04 19:31 | +20 | BNB | UP | 0.59 | open |  |
| 11-04 19:31 | +15 | BNB | UP | 0.59 | open |  |
| 11-04 19:31 | +10 | BNB | UP | 0.59 | open |  |
| 11-04 19:31 | +5 | BNB | UP | 0.59 | open |  |
