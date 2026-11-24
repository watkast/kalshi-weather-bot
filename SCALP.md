# Range-Scalp Bot

*Updated Tue Nov 24 00:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70341 | 61393 | 8948 (147) | 2 | $-18844.99 | -4.3% |
| **+10¢** | 52479 | 42028 | 10451 (190) | 3 | $-17480.40 | -5.3% |
| **+15¢** | 43962 | 32706 | 11256 (246) | 3 | $-15569.91 | -5.6% |
| **+20¢** | 39142 | 27295 | 11847 (311) | 4 | $-13938.63 | -5.7% |
| **+10¢ (15¢ stop)** | 85656 | 85460 | 196 (118) | 1 | $-31496.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 00:32 | +10 stop | BTC | DOWN | 0.68 | open |  |
| 11-24 00:31 | +10 stop | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 11-24 00:31 | +20 | ZEC | DOWN | 0.67 | open |  |
| 11-24 00:31 | +15 | ZEC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-24 00:31 | +10 | ZEC | DOWN | 0.67 | 0.86 | 1.65 |
| 11-24 00:31 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-24 00:31 | +10 stop | ETH | UP | 0.49 | 0.33 | -1.94 |
| 11-24 00:31 | +20 | ETH | UP | 0.49 | open |  |
| 11-24 00:31 | +15 | ETH | UP | 0.51 | open |  |
| 11-24 00:31 | +10 | ETH | UP | 0.51 | open |  |
| 11-24 00:31 | +5 | ETH | UP | 0.51 | open |  |
| 11-24 00:31 | +10 stop | BTC | UP | 0.53 | 0.36 | -2.05 |
| 11-24 00:31 | +20 | BTC | UP | 0.53 | open |  |
| 11-24 00:31 | +15 | BTC | UP | 0.53 | open |  |
| 11-24 00:31 | +10 | BTC | UP | 0.53 | open |  |
| 11-24 00:31 | +5 | BTC | UP | 0.53 | open |  |
| 11-24 00:31 | +10 stop | BNB | UP | 0.51 | 0.35 | -1.94 |
| 11-24 00:31 | +20 | BNB | UP | 0.51 | open |  |
| 11-24 00:31 | +15 | BNB | UP | 0.51 | open |  |
| 11-24 00:31 | +10 | BNB | UP | 0.51 | open |  |
| 11-24 00:31 | +5 | BNB | UP | 0.51 | 0.57 | 0.24 |
| 11-24 00:29 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-24 00:29 | +20 | BTC | DOWN | 0.59 | 0.99 | 3.86 |
| 11-24 00:29 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-24 00:29 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-24 00:29 | +5 | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-24 00:25 | +5 | ETH | DOWN | 0.59 | yes | -6.07 |
| 11-24 00:25 | +5 | BTC | UP | 0.63 | 0.72 | 0.58 |
| 11-24 00:24 | +10 stop | ETH | DOWN | 0.47 | 0.27 | -2.32 |
| 11-24 00:24 | +10 | ETH | DOWN | 0.51 | yes | -5.28 |
| 11-24 00:24 | +5 | ETH | DOWN | 0.50 | 0.56 | 0.24 |
| 11-24 00:24 | +10 stop | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-24 00:24 | +15 | BTC | UP | 0.64 | 0.85 | 1.84 |
| 11-24 00:24 | +10 | BTC | UP | 0.64 | 0.77 | 1.00 |
| 11-24 00:24 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-24 00:24 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-24 00:24 | +20 | SOL | UP | 0.68 | 0.91 | 2.05 |
| 11-24 00:24 | +15 | SOL | UP | 0.68 | 0.91 | 2.05 |
| 11-24 00:24 | +10 | SOL | UP | 0.68 | 0.79 | 0.82 |
| 11-24 00:24 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
