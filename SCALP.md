# Range-Scalp Bot

*Updated Fri Nov 06 05:45 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49253 | 42921 | 6332 (75) | 6 | $-13939.40 | -4.5% |
| **+10¢** | 36774 | 29415 | 7359 (101) | 7 | $-12777.98 | -5.5% |
| **+15¢** | 30801 | 22877 | 7924 (130) | 8 | $-11654.69 | -6.0% |
| **+20¢** | 27380 | 19074 | 8306 (170) | 8 | $-10301.91 | -6.0% |
| **+10¢ (15¢ stop)** | 60057 | 59962 | 95 (57) | 0 | $-22245.90 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 05:43 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 11-06 05:37 | +10 stop | BNB | UP | 0.56 | 0.71 | 1.17 |
| 11-06 05:37 | +5 | ZEC | UP | 0.58 | 0.66 | 0.46 |
| 11-06 05:36 | +10 stop | ZEC | UP | 0.61 | 0.43 | -2.15 |
| 11-06 05:36 | +10 | ZEC | UP | 0.61 | 0.75 | 1.09 |
| 11-06 05:36 | +5 | ZEC | UP | 0.61 | 0.68 | 0.37 |
| 11-06 05:35 | +10 stop | HYPE | UP | 0.67 | 0.81 | 1.13 |
| 11-06 05:35 | +10 stop | BTC | UP | 0.71 | 0.82 | 0.84 |
| 11-06 05:35 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 11-06 05:35 | +10 stop | SOL | UP | 0.70 | 0.81 | 0.84 |
| 11-06 05:35 | +10 stop | BNB | DOWN | 0.55 | 0.35 | -2.34 |
| 11-06 05:35 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-06 05:35 | +15 | BNB | DOWN | 0.55 | open |  |
| 11-06 05:35 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-06 05:35 | +5 | BNB | DOWN | 0.55 | open |  |
| 11-06 05:34 | +10 stop | DOGE | UP | 0.60 | 0.71 | 0.78 |
| 11-06 05:34 | +10 stop | SOL | UP | 0.55 | 0.68 | 0.99 |
| 11-06 05:34 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.74 |
| 11-06 05:34 | +5 | XRP | UP | 0.66 | 0.72 | 0.29 |
| 11-06 05:34 | +10 stop | NEAR | UP | 0.71 | 0.85 | 1.16 |
| 11-06 05:34 | +20 | NEAR | UP | 0.70 | 0.90 | 1.78 |
| 11-06 05:34 | +15 | NEAR | UP | 0.68 | 0.85 | 1.45 |
| 11-06 05:34 | +10 | NEAR | UP | 0.67 | 0.78 | 0.81 |
| 11-06 05:34 | +5 | NEAR | UP | 0.67 | 0.73 | 0.30 |
| 11-06 05:33 | +10 stop | BTC | DOWN | 0.56 | 0.38 | -2.15 |
| 11-06 05:33 | +20 | BTC | DOWN | 0.56 | open |  |
| 11-06 05:33 | +15 | BTC | DOWN | 0.56 | open |  |
| 11-06 05:33 | +10 | BTC | DOWN | 0.56 | open |  |
| 11-06 05:33 | +5 | BTC | DOWN | 0.56 | open |  |
| 11-06 05:33 | +10 stop | HYPE | DOWN | 0.53 | 0.32 | -2.44 |
| 11-06 05:33 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-06 05:33 | +15 | HYPE | DOWN | 0.53 | open |  |
| 11-06 05:33 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-06 05:33 | +5 | HYPE | DOWN | 0.53 | open |  |
| 11-06 05:33 | +10 stop | ETH | DOWN | 0.56 | 0.37 | -2.25 |
| 11-06 05:33 | +20 | ETH | DOWN | 0.56 | open |  |
| 11-06 05:33 | +15 | ETH | DOWN | 0.56 | open |  |
| 11-06 05:33 | +10 | ETH | DOWN | 0.56 | open |  |
| 11-06 05:33 | +5 | ETH | DOWN | 0.56 | open |  |
| 11-06 05:33 | +10 stop | XRP | DOWN | 0.61 | 0.44 | -2.05 |
