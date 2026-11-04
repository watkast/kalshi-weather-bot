# Range-Scalp Bot

*Updated Wed Nov 04 18:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47387 | 41268 | 6119 (72) | 5 | $-13633.56 | -4.6% |
| **+10¢** | 35392 | 28292 | 7100 (97) | 6 | $-12474.43 | -5.6% |
| **+15¢** | 29636 | 21991 | 7645 (125) | 7 | $-11440.80 | -6.2% |
| **+20¢** | 26331 | 18325 | 8006 (165) | 7 | $-10086.13 | -6.1% |
| **+10¢ (15¢ stop)** | 57757 | 57664 | 93 (56) | 0 | $-21534.73 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 18:37 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 18:36 | +5 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-04 18:35 | +5 | ETH | DOWN | 0.57 | 0.74 | 1.38 |
| 11-04 18:35 | +10 stop | BNB | DOWN | 0.64 | 0.79 | 1.21 |
| 11-04 18:35 | +5 | SOL | UP | 0.64 | open |  |
| 11-04 18:35 | +5 | ZEC | UP | 0.54 | open |  |
| 11-04 18:35 | +10 stop | XRP | DOWN | 0.65 | 0.79 | 1.12 |
| 11-04 18:35 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-04 18:34 | +10 | ETH | UP | 0.51 | open |  |
| 11-04 18:34 | +5 | ETH | UP | 0.51 | 0.57 | 0.24 |
| 11-04 18:34 | +10 stop | DOGE | UP | 0.52 | 0.34 | -2.14 |
| 11-04 18:34 | +10 stop | NEAR | UP | 0.56 | 0.16 | -4.28 |
| 11-04 18:34 | +20 | NEAR | UP | 0.56 | open |  |
| 11-04 18:34 | +15 | NEAR | UP | 0.56 | open |  |
| 11-04 18:34 | +10 | NEAR | UP | 0.56 | open |  |
| 11-04 18:34 | +5 | NEAR | UP | 0.56 | open |  |
| 11-04 18:34 | +10 stop | BNB | UP | 0.68 | 0.53 | -1.84 |
| 11-04 18:33 | +10 stop | SOL | UP | 0.68 | 0.53 | -1.84 |
| 11-04 18:33 | +20 | SOL | UP | 0.68 | open |  |
| 11-04 18:33 | +15 | SOL | UP | 0.68 | open |  |
| 11-04 18:33 | +10 | SOL | UP | 0.68 | open |  |
| 11-04 18:33 | +5 | SOL | UP | 0.67 | 0.72 | 0.19 |
| 11-04 18:33 | +10 stop | ZEC | UP | 0.63 | 0.43 | -2.35 |
| 11-04 18:33 | +10 stop | DOGE | DOWN | 0.55 | 0.34 | -2.44 |
| 11-04 18:33 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-04 18:33 | +10 stop | BNB | DOWN | 0.58 | 0.42 | -1.96 |
| 11-04 18:33 | +10 | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-04 18:33 | +5 | BNB | DOWN | 0.58 | 0.64 | 0.25 |
| 11-04 18:32 | +10 stop | XRP | DOWN | 0.68 | 0.49 | -2.24 |
| 11-04 18:32 | +20 | XRP | DOWN | 0.68 | 0.90 | 1.97 |
| 11-04 18:32 | +15 | XRP | DOWN | 0.68 | 0.86 | 1.55 |
| 11-04 18:32 | +10 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-04 18:32 | +5 | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-04 18:32 | +10 stop | BTC | DOWN | 0.66 | 0.47 | -2.24 |
| 11-04 18:32 | +20 | BTC | DOWN | 0.66 | 0.89 | 2.07 |
| 11-04 18:32 | +15 | BTC | DOWN | 0.66 | 0.85 | 1.65 |
| 11-04 18:32 | +10 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-04 18:32 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 11-04 18:32 | +5 | ETH | UP | 0.59 | 0.66 | 0.37 |
| 11-04 18:32 | +10 stop | ETH | UP | 0.57 | 0.42 | -1.86 |
