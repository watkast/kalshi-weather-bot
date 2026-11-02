# Range-Scalp Bot

*Updated Mon Nov 02 10:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44678 | 38906 | 5772 (65) | 5 | $-12913.46 | -4.6% |
| **+10¢** | 33350 | 26669 | 6681 (86) | 5 | $-11730.29 | -5.6% |
| **+15¢** | 27907 | 20718 | 7189 (113) | 7 | $-10753.66 | -6.1% |
| **+20¢** | 24801 | 17274 | 7527 (148) | 9 | $-9470.62 | -6.1% |
| **+10¢ (15¢ stop)** | 54519 | 54432 | 87 (51) | 2 | $-20638.61 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 10:19 | +5 | XRP | UP | 0.70 | open |  |
| 11-02 10:19 | +10 stop | NEAR | DOWN | 0.64 | open |  |
| 11-02 10:19 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-02 10:19 | +5 | NEAR | DOWN | 0.64 | open |  |
| 11-02 10:19 | +10 stop | SOL | DOWN | 0.58 | 0.43 | -1.86 |
| 11-02 10:18 | +10 stop | XRP | UP | 0.53 | 0.66 | 0.96 |
| 11-02 10:18 | +10 | XRP | UP | 0.53 | 0.66 | 0.96 |
| 11-02 10:18 | +5 | XRP | UP | 0.53 | 0.60 | 0.35 |
| 11-02 10:18 | +5 | NEAR | DOWN | 0.61 | 0.68 | 0.37 |
| 11-02 10:17 | +5 | BTC | DOWN | 0.53 | open |  |
| 11-02 10:17 | +5 | ZEC | DOWN | 0.55 | open |  |
| 11-02 10:17 | +5 | HYPE | DOWN | 0.62 | 0.69 | 0.37 |
| 11-02 10:17 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 11-02 10:17 | +20 | NEAR | DOWN | 0.62 | open |  |
| 11-02 10:17 | +15 | NEAR | DOWN | 0.62 | open |  |
| 11-02 10:17 | +10 | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 11-02 10:17 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 11-02 10:17 | +10 stop | BTC | DOWN | 0.53 | 0.36 | -2.05 |
| 11-02 10:17 | +20 | BTC | DOWN | 0.53 | open |  |
| 11-02 10:17 | +15 | BTC | DOWN | 0.53 | open |  |
| 11-02 10:17 | +10 | BTC | DOWN | 0.52 | open |  |
| 11-02 10:17 | +5 | BTC | DOWN | 0.52 | 0.57 | 0.14 |
| 11-02 10:17 | +5 | ETH | DOWN | 0.46 | 0.57 | 0.74 |
| 11-02 10:17 | +5 | ZEC | DOWN | 0.52 | 0.57 | 0.14 |
| 11-02 10:17 | +10 stop | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-02 10:17 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-02 10:17 | +15 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-02 10:17 | +10 | HYPE | DOWN | 0.57 | 0.69 | 0.87 |
| 11-02 10:17 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 11-02 10:16 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-02 10:16 | +20 | DOGE | UP | 0.60 | open |  |
| 11-02 10:16 | +15 | DOGE | UP | 0.60 | open |  |
| 11-02 10:16 | +10 | DOGE | UP | 0.60 | open |  |
| 11-02 10:16 | +5 | DOGE | UP | 0.60 | 0.66 | 0.27 |
| 11-02 10:16 | +10 stop | ETH | UP | 0.51 | 0.61 | 0.65 |
| 11-02 10:16 | +20 | ETH | UP | 0.51 | open |  |
| 11-02 10:16 | +15 | ETH | UP | 0.51 | open |  |
| 11-02 10:16 | +10 | ETH | UP | 0.51 | 0.61 | 0.65 |
| 11-02 10:16 | +5 | ETH | UP | 0.52 | 0.60 | 0.45 |
| 11-02 10:16 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
