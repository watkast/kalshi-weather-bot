# Range-Scalp Bot

*Updated Sat Nov 07 21:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51523 | 44930 | 6593 (80) | 4 | $-14253.19 | -4.4% |
| **+10¢** | 38445 | 30757 | 7688 (106) | 6 | $-13265.90 | -5.5% |
| **+15¢** | 32185 | 23900 | 8285 (135) | 8 | $-12166.28 | -6.0% |
| **+20¢** | 28628 | 19944 | 8684 (178) | 8 | $-10718.29 | -6.0% |
| **+10¢ (15¢ stop)** | 62734 | 62631 | 103 (61) | 0 | $-23199.62 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 21:09 | +10 stop | BTC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-07 21:09 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-07 21:08 | +10 stop | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 11-07 21:08 | +5 | NEAR | UP | 0.69 | 0.82 | 1.04 |
| 11-07 21:08 | +20 | NEAR | DOWN | 0.47 | open |  |
| 11-07 21:08 | +10 stop | NEAR | DOWN | 0.52 | 0.36 | -1.95 |
| 11-07 21:08 | +15 | NEAR | DOWN | 0.52 | open |  |
| 11-07 21:08 | +10 | NEAR | DOWN | 0.52 | open |  |
| 11-07 21:08 | +5 | NEAR | DOWN | 0.52 | 0.60 | 0.45 |
| 11-07 21:07 | +10 stop | HYPE | UP | 0.58 | 0.33 | -2.84 |
| 11-07 21:07 | +20 | HYPE | UP | 0.58 | open |  |
| 11-07 21:07 | +15 | HYPE | UP | 0.58 | open |  |
| 11-07 21:07 | +10 | HYPE | UP | 0.58 | open |  |
| 11-07 21:07 | +5 | HYPE | UP | 0.58 | open |  |
| 11-07 21:07 | +10 stop | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-07 21:07 | +5 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-07 21:07 | +10 stop | BNB | DOWN | 0.54 | 0.80 | 2.30 |
| 11-07 21:07 | +10 | BNB | DOWN | 0.54 | 0.80 | 2.30 |
| 11-07 21:07 | +5 | BNB | DOWN | 0.54 | 0.80 | 2.30 |
| 11-07 21:07 | +10 stop | XRP | DOWN | 0.69 | 0.90 | 1.89 |
| 11-07 21:06 | +10 stop | ETH | UP | 0.60 | 0.44 | -1.95 |
| 11-07 21:06 | +10 | ETH | UP | 0.60 | open |  |
| 11-07 21:06 | +5 | ETH | UP | 0.69 | open |  |
| 11-07 21:06 | +10 stop | ZEC | DOWN | 0.38 | 0.55 | 1.35 |
| 11-07 21:06 | +5 | SOL | DOWN | 0.54 | 0.59 | 0.15 |
| 11-07 21:05 | +10 stop | SOL | DOWN | 0.61 | 0.43 | -2.15 |
| 11-07 21:05 | +5 | SOL | DOWN | 0.61 | 0.66 | 0.17 |
| 11-07 21:05 | +10 stop | DOGE | DOWN | 0.51 | 0.83 | 2.92 |
| 11-07 21:04 | +10 stop | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 11-07 21:04 | +15 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 11-07 21:04 | +10 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 11-07 21:04 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 11-07 21:04 | +10 | SOL | DOWN | 0.57 | 0.90 | 3.05 |
| 11-07 21:04 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 11-07 21:04 | +10 stop | ETH | UP | 0.45 | 0.55 | 0.64 |
| 11-07 21:04 | +10 | ETH | UP | 0.45 | 0.55 | 0.64 |
| 11-07 21:04 | +5 | BTC | UP | 0.50 | 0.64 | 1.05 |
| 11-07 21:04 | +10 stop | BNB | UP | 0.56 | 0.70 | 1.02 |
| 11-07 21:04 | +10 | BNB | UP | 0.56 | 0.70 | 1.02 |
| 11-07 21:04 | +5 | BNB | UP | 0.56 | 0.70 | 1.02 |
