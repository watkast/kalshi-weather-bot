# Range-Scalp Bot

*Updated Mon Nov 23 13:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70052 | 61133 | 8919 (146) | 0 | $-18824.88 | -4.3% |
| **+10¢** | 52263 | 41845 | 10418 (189) | 1 | $-17490.07 | -5.3% |
| **+15¢** | 43795 | 32574 | 11221 (245) | 1 | $-15589.00 | -5.7% |
| **+20¢** | 38992 | 27184 | 11808 (310) | 1 | $-13951.29 | -5.7% |
| **+10¢ (15¢ stop)** | 85326 | 85136 | 190 (118) | 1 | $-31351.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 13:34 | +15 | NEAR | DOWN | 0.70 | open |  |
| 11-23 13:34 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-23 13:34 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-23 13:33 | +10 stop | NEAR | DOWN | 0.71 | open |  |
| 11-23 13:31 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.03 |
| 11-23 13:31 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 11-23 13:31 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 11-23 13:31 | +10 | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-23 13:31 | +5 | BNB | DOWN | 0.65 | 0.79 | 1.12 |
| 11-23 13:31 | +10 stop | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 11-23 13:31 | +20 | NEAR | DOWN | 0.58 | open |  |
| 11-23 13:31 | +15 | NEAR | DOWN | 0.58 | 0.74 | 1.28 |
| 11-23 13:31 | +10 | NEAR | DOWN | 0.58 | 0.74 | 1.29 |
| 11-23 13:31 | +5 | NEAR | DOWN | 0.58 | 0.74 | 1.29 |
| 11-23 13:28 | +10 stop | BNB | UP | 0.13 | 0.59 | 4.40 |
| 11-23 13:27 | +10 stop | XRP | UP | 0.70 | 0.55 | -1.83 |
| 11-23 13:26 | +10 stop | DOGE | UP | 0.57 | 0.81 | 2.11 |
| 11-23 13:26 | +10 stop | HYPE | UP | 0.55 | 0.78 | 1.99 |
| 11-23 13:26 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 11-23 13:26 | +5 | ETH | DOWN | 0.55 | yes | -5.68 |
| 11-23 13:26 | +5 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 11-23 13:25 | +10 stop | XRP | DOWN | 0.61 | 0.44 | -2.05 |
| 11-23 13:25 | +10 stop | BNB | DOWN | 0.68 | 0.46 | -2.54 |
| 11-23 13:25 | +15 | BNB | DOWN | 0.68 | 0.92 | 2.14 |
| 11-23 13:25 | +10 | BNB | DOWN | 0.68 | 0.92 | 2.14 |
| 11-23 13:25 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 11-23 13:25 | +10 stop | ETH | DOWN | 0.66 | 0.31 | -3.81 |
| 11-23 13:25 | +10 | ETH | DOWN | 0.66 | yes | -6.76 |
| 11-23 13:25 | +5 | ETH | DOWN | 0.66 | 0.75 | 0.60 |
| 11-23 13:25 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-23 13:24 | +5 | SOL | UP | 0.61 | 0.70 | 0.58 |
| 11-23 13:24 | +10 stop | SOL | UP | 0.63 | 0.80 | 1.41 |
| 11-23 13:24 | +10 | SOL | UP | 0.63 | 0.80 | 1.41 |
| 11-23 13:24 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 11-23 13:24 | +10 | NEAR | DOWN | 0.63 | yes | -6.46 |
| 11-23 13:24 | +5 | NEAR | DOWN | 0.62 | yes | -6.34 |
| 11-23 13:24 | +10 stop | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 11-23 13:24 | +10 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 11-23 13:24 | +5 | ETH | DOWN | 0.60 | 0.69 | 0.58 |
| 11-23 13:23 | +15 | HYPE | DOWN | 0.69 | yes | -7.07 |
