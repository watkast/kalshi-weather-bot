# Range-Scalp Bot

*Updated Mon Nov 02 02:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44226 | 38514 | 5712 (65) | 6 | $-12789.95 | -4.6% |
| **+10¢** | 33002 | 26398 | 6604 (86) | 6 | $-11577.00 | -5.6% |
| **+15¢** | 27624 | 20517 | 7107 (113) | 7 | $-10585.99 | -6.1% |
| **+20¢** | 24546 | 17107 | 7439 (147) | 7 | $-9302.70 | -6.0% |
| **+10¢ (15¢ stop)** | 53958 | 53872 | 86 (51) | 2 | $-20458.27 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 02:06 | +10 stop | BTC | UP | 0.57 | open |  |
| 11-02 02:06 | +10 stop | BNB | DOWN | 0.62 | open |  |
| 11-02 02:06 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-02 02:06 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-02 02:06 | +10 | BNB | DOWN | 0.62 | open |  |
| 11-02 02:06 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-02 02:06 | +10 stop | XRP | DOWN | 0.46 | 0.61 | 1.15 |
| 11-02 02:06 | +10 | XRP | DOWN | 0.46 | 0.61 | 1.15 |
| 11-02 02:06 | +5 | XRP | DOWN | 0.46 | 0.61 | 1.15 |
| 11-02 02:05 | +5 | BTC | DOWN | 0.71 | open |  |
| 11-02 02:05 | +10 stop | ETH | DOWN | 0.55 | 0.27 | -3.12 |
| 11-02 02:05 | +5 | ETH | DOWN | 0.55 | open |  |
| 11-02 02:04 | +10 stop | ZEC | UP | 0.62 | 0.82 | 1.72 |
| 11-02 02:04 | +5 | SOL | DOWN | 0.64 | open |  |
| 11-02 02:03 | +10 stop | ZEC | UP | 0.51 | 0.63 | 0.85 |
| 11-02 02:03 | +5 | ETH | DOWN | 0.53 | 0.60 | 0.35 |
| 11-02 02:03 | +10 stop | SOL | DOWN | 0.60 | 0.36 | -2.74 |
| 11-02 02:03 | +10 stop | NEAR | UP | 0.56 | 0.72 | 1.27 |
| 11-02 02:03 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.68 |
| 11-02 02:02 | +10 stop | ZEC | UP | 0.64 | 0.47 | -2.05 |
| 11-02 02:02 | +10 stop | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 02:02 | +20 | XRP | DOWN | 0.70 | open |  |
| 11-02 02:02 | +15 | XRP | DOWN | 0.70 | open |  |
| 11-02 02:02 | +10 | XRP | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 02:02 | +5 | XRP | DOWN | 0.70 | 0.76 | 0.32 |
| 11-02 02:02 | +5 | ZEC | UP | 0.64 | 0.82 | 1.52 |
| 11-02 02:02 | +10 stop | ETH | UP | 0.56 | 0.39 | -2.05 |
| 11-02 02:02 | +20 | ETH | UP | 0.56 | 0.83 | 2.42 |
| 11-02 02:02 | +15 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-02 02:02 | +10 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-02 02:02 | +5 | ETH | UP | 0.56 | 0.63 | 0.35 |
| 11-02 02:01 | +10 stop | ZEC | DOWN | 0.58 | 0.43 | -1.86 |
| 11-02 02:01 | +20 | ZEC | DOWN | 0.58 | open |  |
| 11-02 02:01 | +15 | ZEC | DOWN | 0.58 | open |  |
| 11-02 02:01 | +10 | ZEC | DOWN | 0.58 | open |  |
| 11-02 02:01 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 11-02 02:01 | +10 stop | NEAR | DOWN | 0.51 | 0.28 | -2.63 |
| 11-02 02:01 | +20 | NEAR | DOWN | 0.51 | open |  |
| 11-02 02:01 | +15 | NEAR | DOWN | 0.51 | open |  |
| 11-02 02:01 | +10 | NEAR | DOWN | 0.52 | open |  |
