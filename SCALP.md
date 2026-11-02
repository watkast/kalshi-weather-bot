# Range-Scalp Bot

*Updated Mon Nov 02 02:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44248 | 38534 | 5714 (65) | 2 | $-12791.59 | -4.6% |
| **+10¢** | 33017 | 26411 | 6606 (86) | 3 | $-11574.66 | -5.6% |
| **+15¢** | 27635 | 20525 | 7110 (113) | 3 | $-10589.35 | -6.1% |
| **+20¢** | 24556 | 17114 | 7442 (147) | 4 | $-9305.21 | -6.0% |
| **+10¢ (15¢ stop)** | 53981 | 53895 | 86 (51) | 1 | $-20462.52 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 02:26 | +10 stop | HYPE | DOWN | 0.64 | 0.48 | -1.99 |
| 11-02 02:26 | +10 stop | BNB | DOWN | 0.46 | 0.56 | 0.64 |
| 11-02 02:26 | +20 | BNB | DOWN | 0.48 | open |  |
| 11-02 02:26 | +15 | BNB | DOWN | 0.48 | open |  |
| 11-02 02:26 | +10 | BNB | DOWN | 0.48 | open |  |
| 11-02 02:26 | +5 | BNB | DOWN | 0.48 | 0.56 | 0.44 |
| 11-02 02:26 | +10 stop | ETH | UP | 0.60 | open |  |
| 11-02 02:26 | +10 | ETH | UP | 0.60 | open |  |
| 11-02 02:26 | +5 | ETH | UP | 0.60 | open |  |
| 11-02 02:25 | +10 stop | ZEC | UP | 0.66 | 0.84 | 1.54 |
| 11-02 02:25 | +20 | ZEC | UP | 0.66 | open |  |
| 11-02 02:25 | +15 | ZEC | UP | 0.66 | 0.84 | 1.54 |
| 11-02 02:25 | +10 | ZEC | UP | 0.66 | 0.84 | 1.54 |
| 11-02 02:25 | +5 | ZEC | UP | 0.66 | 0.72 | 0.29 |
| 11-02 02:25 | +5 | HYPE | UP | 0.55 | open |  |
| 11-02 02:24 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-02 02:21 | +10 stop | HYPE | UP | 0.60 | 0.45 | -1.85 |
| 11-02 02:21 | +20 | HYPE | UP | 0.60 | open |  |
| 11-02 02:21 | +15 | HYPE | UP | 0.62 | open |  |
| 11-02 02:21 | +10 | HYPE | UP | 0.62 | open |  |
| 11-02 02:21 | +5 | HYPE | UP | 0.62 | 0.68 | 0.27 |
| 11-02 02:19 | +10 stop | ETH | UP | 0.61 | 0.79 | 1.51 |
| 11-02 02:19 | +5 | ETH | UP | 0.61 | 0.70 | 0.58 |
| 11-02 02:19 | +10 stop | ZEC | UP | 0.68 | 0.80 | 0.93 |
| 11-02 02:19 | +10 | ZEC | UP | 0.68 | 0.80 | 0.93 |
| 11-02 02:19 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
| 11-02 02:19 | +5 | ETH | UP | 0.55 | 0.62 | 0.35 |
| 11-02 02:16 | +10 stop | ETH | UP | 0.69 | 0.53 | -1.93 |
| 11-02 02:16 | +20 | ETH | UP | 0.69 | open |  |
| 11-02 02:16 | +15 | ETH | UP | 0.69 | open |  |
| 11-02 02:16 | +10 | ETH | UP | 0.69 | 0.79 | 0.73 |
| 11-02 02:16 | +5 | ETH | UP | 0.69 | 0.74 | 0.21 |
| 11-02 02:16 | +10 stop | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 11-02 02:16 | +20 | ZEC | UP | 0.64 | 0.87 | 2.05 |
| 11-02 02:16 | +15 | ZEC | UP | 0.64 | 0.80 | 1.31 |
| 11-02 02:16 | +10 | ZEC | UP | 0.64 | 0.76 | 0.90 |
| 11-02 02:16 | +5 | ZEC | UP | 0.64 | 0.71 | 0.38 |
| 11-02 02:16 | +10 stop | BNB | UP | 0.58 | 0.75 | 1.38 |
| 11-02 02:16 | +20 | BNB | UP | 0.58 | 0.78 | 1.69 |
| 11-02 02:16 | +15 | BNB | UP | 0.58 | 0.75 | 1.38 |
