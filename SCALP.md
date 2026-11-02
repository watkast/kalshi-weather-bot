# Range-Scalp Bot

*Updated Mon Nov 02 00:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44122 | 38429 | 5693 (65) | 0 | $-12711.72 | -4.6% |
| **+10¢** | 32927 | 26347 | 6580 (86) | 1 | $-11476.45 | -5.5% |
| **+15¢** | 27559 | 20477 | 7082 (113) | 1 | $-10488.33 | -6.1% |
| **+20¢** | 24485 | 17070 | 7415 (147) | 1 | $-9229.75 | -6.0% |
| **+10¢ (15¢ stop)** | 53809 | 53723 | 86 (51) | 0 | $-20344.71 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 00:17 | +10 stop | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-02 00:17 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-02 00:17 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-02 00:17 | +10 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-02 00:17 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.62 |
| 11-02 00:17 | +5 | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 11-02 00:16 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-02 00:16 | +20 | HYPE | DOWN | 0.62 | 0.83 | 1.79 |
| 11-02 00:16 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.26 |
| 11-02 00:16 | +10 | HYPE | DOWN | 0.62 | 0.73 | 0.75 |
| 11-02 00:16 | +5 | HYPE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-02 00:16 | +10 stop | NEAR | UP | 0.44 | 0.28 | -1.93 |
| 11-02 00:16 | +20 | NEAR | UP | 0.44 | open |  |
| 11-02 00:16 | +15 | NEAR | UP | 0.44 | open |  |
| 11-02 00:16 | +10 | NEAR | UP | 0.44 | open |  |
| 11-02 00:16 | +5 | NEAR | UP | 0.44 | 0.53 | 0.54 |
| 11-02 00:16 | +10 stop | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 00:16 | +20 | XRP | DOWN | 0.67 | 0.89 | 1.97 |
| 11-02 00:16 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 00:16 | +10 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 00:16 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 11-02 00:16 | +10 stop | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 11-02 00:16 | +20 | ETH | DOWN | 0.61 | 0.81 | 1.72 |
| 11-02 00:16 | +15 | ETH | DOWN | 0.61 | 0.80 | 1.61 |
| 11-02 00:16 | +10 | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 11-02 00:16 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-02 00:13 | +10 stop | ZEC | DOWN | 0.40 | 0.67 | 2.37 |
| 11-02 00:13 | +5 | ZEC | DOWN | 0.41 | 0.67 | 2.29 |
| 11-02 00:11 | +10 stop | ZEC | DOWN | 0.70 | 0.49 | -2.43 |
| 11-02 00:10 | +10 stop | ZEC | UP | 0.67 | 0.49 | -2.12 |
| 11-02 00:10 | +20 | ZEC | UP | 0.67 | no | -6.86 |
| 11-02 00:10 | +15 | ZEC | UP | 0.68 | no | -7.00 |
| 11-02 00:10 | +10 | ZEC | UP | 0.65 | 0.76 | 0.83 |
| 11-02 00:10 | +5 | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 11-02 00:09 | +10 stop | ETH | DOWN | 0.62 | 0.81 | 1.62 |
| 11-02 00:09 | +5 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-02 00:09 | +10 stop | DOGE | UP | 0.65 | 0.39 | -2.93 |
| 11-02 00:09 | +20 | DOGE | UP | 0.65 | no | -6.66 |
| 11-02 00:09 | +15 | DOGE | UP | 0.65 | no | -6.66 |
| 11-02 00:09 | +10 | DOGE | UP | 0.65 | no | -6.66 |
