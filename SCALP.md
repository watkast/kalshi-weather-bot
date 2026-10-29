# Range-Scalp Bot

*Updated Thu Oct 29 02:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38851 | 33909 | 4942 (49) | 2 | $-10863.80 | -4.4% |
| **+10¢** | 28983 | 23277 | 5706 (71) | 3 | $-9606.43 | -5.3% |
| **+15¢** | 24246 | 18115 | 6131 (97) | 3 | $-8551.90 | -5.6% |
| **+20¢** | 21514 | 15092 | 6422 (125) | 3 | $-7447.75 | -5.5% |
| **+10¢ (15¢ stop)** | 47516 | 47449 | 67 (35) | 0 | $-18015.52 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 02:51 | +10 stop | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-29 02:51 | +15 | NEAR | UP | 0.66 | 0.82 | 1.33 |
| 10-29 02:51 | +10 | NEAR | UP | 0.66 | 0.77 | 0.81 |
| 10-29 02:51 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-29 02:47 | +5 | BTC | UP | 0.65 | 0.75 | 0.70 |
| 10-29 02:47 | +10 stop | XRP | UP | 0.58 | 0.72 | 1.07 |
| 10-29 02:47 | +10 stop | DOGE | UP | 0.54 | 0.67 | 0.96 |
| 10-29 02:47 | +10 | DOGE | UP | 0.53 | 0.67 | 1.06 |
| 10-29 02:47 | +5 | DOGE | UP | 0.54 | 0.61 | 0.35 |
| 10-29 02:47 | +5 | HYPE | UP | 0.60 | 0.81 | 1.78 |
| 10-29 02:47 | +5 | ETH | UP | 0.54 | 0.68 | 1.06 |
| 10-29 02:47 | +10 stop | BNB | UP | 0.66 | 0.83 | 1.40 |
| 10-29 02:47 | +20 | BNB | UP | 0.66 | 0.87 | 1.82 |
| 10-29 02:47 | +15 | BNB | UP | 0.66 | 0.83 | 1.40 |
| 10-29 02:47 | +10 | BNB | UP | 0.66 | 0.83 | 1.44 |
| 10-29 02:47 | +5 | BNB | UP | 0.66 | 0.73 | 0.40 |
| 10-29 02:47 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-29 02:47 | +20 | NEAR | UP | 0.62 | 0.82 | 1.72 |
| 10-29 02:47 | +15 | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 10-29 02:47 | +10 | NEAR | UP | 0.62 | 0.74 | 0.89 |
| 10-29 02:47 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 10-29 02:47 | +5 | SOL | UP | 0.68 | 0.76 | 0.52 |
| 10-29 02:47 | +10 stop | BTC | UP | 0.59 | 0.75 | 1.29 |
| 10-29 02:47 | +20 | BTC | UP | 0.59 | 0.82 | 2.02 |
| 10-29 02:47 | +15 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 10-29 02:47 | +10 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 10-29 02:47 | +5 | BTC | UP | 0.59 | 0.65 | 0.27 |
| 10-29 02:46 | +10 stop | DOGE | DOWN | 0.50 | 0.61 | 0.75 |
| 10-29 02:46 | +20 | DOGE | DOWN | 0.49 | open |  |
| 10-29 02:46 | +15 | DOGE | DOWN | 0.49 | open |  |
| 10-29 02:46 | +10 | DOGE | DOWN | 0.49 | 0.61 | 0.85 |
| 10-29 02:46 | +5 | DOGE | DOWN | 0.49 | 0.61 | 0.85 |
| 10-29 02:46 | +10 stop | ETH | DOWN | 0.49 | 0.31 | -2.13 |
| 10-29 02:46 | +20 | ETH | DOWN | 0.49 | open |  |
| 10-29 02:46 | +15 | ETH | DOWN | 0.49 | open |  |
| 10-29 02:46 | +10 | ETH | DOWN | 0.49 | open |  |
| 10-29 02:46 | +5 | ETH | DOWN | 0.49 | 0.56 | 0.34 |
| 10-29 02:46 | +10 stop | ZEC | DOWN | 0.52 | 0.31 | -2.43 |
| 10-29 02:46 | +20 | ZEC | DOWN | 0.52 | open |  |
| 10-29 02:46 | +15 | ZEC | DOWN | 0.52 | open |  |
