# Range-Scalp Bot

*Updated Mon Nov 02 10:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44657 | 38885 | 5772 (65) | 1 | $-12928.86 | -4.6% |
| **+10¢** | 33336 | 26655 | 6681 (86) | 1 | $-11748.34 | -5.6% |
| **+15¢** | 27900 | 20711 | 7189 (113) | 1 | $-10767.87 | -6.1% |
| **+20¢** | 24796 | 17269 | 7527 (148) | 2 | $-9483.29 | -6.1% |
| **+10¢ (15¢ stop)** | 54499 | 54412 | 87 (51) | 1 | $-20640.80 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 10:09 | +5 | HYPE | DOWN | 0.50 | open |  |
| 11-02 10:08 | +10 stop | HYPE | DOWN | 0.69 | open |  |
| 11-02 10:08 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-02 10:04 | +10 stop | HYPE | DOWN | 0.63 | 0.75 | 0.93 |
| 11-02 10:03 | +10 stop | NEAR | DOWN | 0.50 | 0.79 | 2.57 |
| 11-02 10:03 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-02 10:01 | +10 stop | HYPE | DOWN | 0.71 | 0.54 | -2.03 |
| 11-02 10:01 | +20 | HYPE | DOWN | 0.71 | open |  |
| 11-02 10:01 | +15 | HYPE | DOWN | 0.71 | open |  |
| 11-02 10:01 | +10 | HYPE | DOWN | 0.71 | open |  |
| 11-02 10:01 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.54 |
| 11-02 10:01 | +10 stop | NEAR | DOWN | 0.68 | 0.52 | -1.94 |
| 11-02 10:01 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-02 10:01 | +15 | NEAR | DOWN | 0.68 | 0.85 | 1.45 |
| 11-02 10:01 | +10 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-02 10:01 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-02 10:01 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 10:01 | +20 | ZEC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-02 10:01 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-02 10:01 | +10 | ZEC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-02 10:01 | +5 | ZEC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-02 08:05 | +10 stop | ZEC | UP | 0.58 | no | -5.98 |
| 11-02 08:05 | +10 | ZEC | UP | 0.57 | no | -5.88 |
| 11-02 08:04 | +5 | ZEC | UP | 0.61 | no | -6.27 |
| 11-02 08:04 | +5 | SOL | UP | 0.69 | no | -7.05 |
| 11-02 08:04 | +10 stop | ZEC | UP | 0.49 | 0.60 | 0.75 |
| 11-02 08:04 | +15 | ZEC | UP | 0.49 | no | -5.08 |
| 11-02 08:04 | +10 | ZEC | UP | 0.49 | 0.60 | 0.75 |
| 11-02 08:04 | +5 | ZEC | UP | 0.49 | 0.56 | 0.34 |
| 11-02 08:04 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-02 08:04 | +10 | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-02 08:04 | +5 | SOL | UP | 0.61 | 0.68 | 0.37 |
| 11-02 08:02 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 11-02 08:02 | +20 | XRP | UP | 0.68 | no | -6.96 |
| 11-02 08:02 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-02 08:02 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-02 08:02 | +5 | XRP | UP | 0.68 | 0.77 | 0.61 |
| 11-02 08:01 | +10 stop | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 11-02 08:01 | +20 | ZEC | UP | 0.60 | no | -6.17 |
| 11-02 08:01 | +15 | ZEC | UP | 0.60 | 0.77 | 1.40 |
