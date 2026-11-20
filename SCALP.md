# Range-Scalp Bot

*Updated Fri Nov 20 00:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65546 | 57216 | 8330 (124) | 3 | $-17550.36 | -4.3% |
| **+10¢** | 48955 | 39214 | 9741 (165) | 1 | $-16321.83 | -5.3% |
| **+15¢** | 41053 | 30547 | 10506 (211) | 3 | $-14681.57 | -5.7% |
| **+20¢** | 36551 | 25512 | 11039 (266) | 2 | $-13010.63 | -5.7% |
| **+10¢ (15¢ stop)** | 79797 | 79633 | 164 (98) | 0 | $-29363.16 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 00:40 | +10 stop | ETH | DOWN | 0.67 | 0.79 | 0.92 |
| 11-20 00:40 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-20 00:40 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 11-20 00:39 | +10 stop | BTC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-20 00:39 | +5 | BTC | DOWN | 0.67 | 0.75 | 0.50 |
| 11-20 00:37 | +5 | BNB | UP | 0.57 | open |  |
| 11-20 00:36 | +10 stop | XRP | DOWN | 0.60 | 0.74 | 1.09 |
| 11-20 00:36 | +10 stop | BTC | UP | 0.55 | 0.38 | -2.05 |
| 11-20 00:36 | +10 stop | SOL | DOWN | 0.70 | 0.84 | 1.15 |
| 11-20 00:36 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-20 00:36 | +20 | DOGE | DOWN | 0.67 | 0.91 | 2.15 |
| 11-20 00:36 | +15 | DOGE | DOWN | 0.67 | 0.86 | 1.65 |
| 11-20 00:36 | +10 | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-20 00:36 | +5 | BNB | UP | 0.54 | 0.59 | 0.15 |
| 11-20 00:36 | +5 | ZEC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-20 00:36 | +10 | ETH | DOWN | 0.50 | 0.64 | 1.05 |
| 11-20 00:36 | +10 stop | BNB | DOWN | 0.50 | 0.64 | 1.05 |
| 11-20 00:36 | +10 | BNB | DOWN | 0.47 | 0.64 | 1.35 |
| 11-20 00:36 | +5 | BNB | DOWN | 0.47 | 0.55 | 0.44 |
| 11-20 00:35 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-20 00:35 | +10 stop | XRP | DOWN | 0.66 | 0.47 | -2.24 |
| 11-20 00:35 | +10 stop | BTC | DOWN | 0.58 | 0.42 | -1.96 |
| 11-20 00:35 | +5 | BTC | DOWN | 0.59 | 0.77 | 1.50 |
| 11-20 00:35 | +10 stop | ETH | DOWN | 0.62 | 0.47 | -1.85 |
| 11-20 00:34 | +10 stop | BTC | UP | 0.61 | 0.45 | -1.95 |
| 11-20 00:34 | +20 | BTC | UP | 0.61 | open |  |
| 11-20 00:34 | +15 | BTC | UP | 0.61 | open |  |
| 11-20 00:34 | +10 | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-20 00:34 | +5 | BTC | UP | 0.61 | 0.66 | 0.17 |
| 11-20 00:34 | +5 | ETH | UP | 0.62 | open |  |
| 11-20 00:34 | +10 stop | XRP | UP | 0.59 | 0.40 | -2.24 |
| 11-20 00:34 | +20 | XRP | UP | 0.59 | 0.93 | 3.15 |
| 11-20 00:34 | +15 | XRP | UP | 0.59 | 0.93 | 3.15 |
| 11-20 00:34 | +10 | XRP | UP | 0.59 | 0.93 | 3.15 |
| 11-20 00:34 | +5 | XRP | UP | 0.59 | 0.93 | 3.15 |
| 11-20 00:33 | +10 stop | NEAR | DOWN | 0.49 | 0.68 | 1.56 |
| 11-20 00:33 | +20 | NEAR | DOWN | 0.50 | 0.78 | 2.52 |
| 11-20 00:33 | +15 | NEAR | DOWN | 0.49 | 0.68 | 1.56 |
| 11-20 00:33 | +10 | NEAR | DOWN | 0.49 | 0.68 | 1.56 |
| 11-20 00:33 | +5 | NEAR | DOWN | 0.49 | 0.54 | 0.14 |
