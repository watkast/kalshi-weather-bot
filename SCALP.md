# Range-Scalp Bot

*Updated Mon Nov 02 11:21 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44773 | 38989 | 5784 (65) | 3 | $-12942.16 | -4.6% |
| **+10¢** | 33419 | 26721 | 6698 (86) | 3 | $-11786.39 | -5.6% |
| **+15¢** | 27959 | 20749 | 7210 (113) | 4 | $-10836.18 | -6.2% |
| **+20¢** | 24842 | 17295 | 7547 (148) | 4 | $-9550.71 | -6.1% |
| **+10¢ (15¢ stop)** | 54640 | 54553 | 87 (51) | 2 | $-20684.01 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 11:20 | +10 stop | HYPE | UP | 0.60 | open |  |
| 11-02 11:19 | +10 stop | NEAR | DOWN | 0.50 | open |  |
| 11-02 11:19 | +10 | NEAR | DOWN | 0.50 | open |  |
| 11-02 11:19 | +5 | NEAR | DOWN | 0.49 | open |  |
| 11-02 11:19 | +10 stop | XRP | DOWN | 0.66 | 0.48 | -2.09 |
| 11-02 11:18 | +10 stop | HYPE | DOWN | 0.58 | 0.43 | -1.86 |
| 11-02 11:18 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-02 11:18 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-02 11:18 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-02 11:18 | +5 | HYPE | DOWN | 0.58 | open |  |
| 11-02 11:17 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-02 11:17 | +20 | NEAR | DOWN | 0.71 | open |  |
| 11-02 11:17 | +15 | NEAR | DOWN | 0.71 | open |  |
| 11-02 11:17 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-02 11:17 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.53 |
| 11-02 11:17 | +10 stop | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 11:17 | +20 | BNB | DOWN | 0.67 | open |  |
| 11-02 11:17 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-02 11:17 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 11:17 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 11-02 11:16 | +10 stop | ZEC | DOWN | 0.56 | 0.70 | 1.07 |
| 11-02 11:16 | +20 | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-02 11:16 | +15 | ZEC | DOWN | 0.56 | 0.76 | 1.69 |
| 11-02 11:16 | +10 | ZEC | DOWN | 0.56 | 0.70 | 1.07 |
| 11-02 11:16 | +5 | ZEC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-02 11:16 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-02 11:16 | +20 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 11-02 11:16 | +15 | ETH | DOWN | 0.60 | 0.79 | 1.61 |
| 11-02 11:16 | +10 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-02 11:16 | +5 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-02 11:16 | +10 stop | XRP | UP | 0.53 | 0.33 | -2.34 |
| 11-02 11:16 | +20 | XRP | UP | 0.53 | open |  |
| 11-02 11:16 | +15 | XRP | UP | 0.53 | open |  |
| 11-02 11:16 | +10 | XRP | UP | 0.53 | open |  |
| 11-02 11:16 | +5 | XRP | UP | 0.53 | open |  |
| 11-02 11:13 | +10 stop | BTC | DOWN | 0.51 | 0.82 | 2.81 |
| 11-02 11:12 | +10 stop | ZEC | UP | 0.59 | 0.82 | 2.02 |
| 11-02 11:11 | +10 stop | ZEC | DOWN | 0.71 | 0.46 | -2.83 |
| 11-02 11:11 | +15 | ZEC | DOWN | 0.71 | yes | -7.25 |
| 11-02 11:11 | +10 | ZEC | DOWN | 0.71 | yes | -7.25 |
