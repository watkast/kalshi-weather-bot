# Range-Scalp Bot

*Updated Mon Nov 02 07:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44601 | 38836 | 5765 (65) | 2 | $-12912.25 | -4.6% |
| **+10¢** | 33295 | 26627 | 6668 (86) | 5 | $-11699.79 | -5.6% |
| **+15¢** | 27866 | 20691 | 7175 (113) | 5 | $-10713.65 | -6.1% |
| **+20¢** | 24766 | 17254 | 7512 (147) | 4 | $-9431.20 | -6.1% |
| **+10¢ (15¢ stop)** | 54445 | 54359 | 86 (51) | 0 | $-20646.29 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 07:27 | +5 | SOL | DOWN | 0.25 | 0.59 | 3.09 |
| 11-02 07:27 | +5 | ZEC | DOWN | 0.50 | 0.64 | 1.05 |
| 11-02 07:26 | +10 stop | ZEC | DOWN | 0.69 | 0.48 | -2.43 |
| 11-02 07:26 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-02 07:26 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-02 07:26 | +10 | ZEC | DOWN | 0.67 | open |  |
| 11-02 07:26 | +10 stop | SOL | DOWN | 0.65 | 0.15 | -5.25 |
| 11-02 07:26 | +15 | SOL | DOWN | 0.65 | open |  |
| 11-02 07:26 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-02 07:26 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 11-02 07:25 | +5 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-02 07:25 | +10 stop | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-02 07:25 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-02 07:25 | +5 | BTC | DOWN | 0.56 | 0.64 | 0.45 |
| 11-02 07:24 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 07:24 | +15 | DOGE | DOWN | 0.70 | 0.92 | 2.03 |
| 11-02 07:24 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 07:24 | +5 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-02 07:24 | +10 stop | BTC | DOWN | 0.53 | 0.64 | 0.79 |
| 11-02 07:23 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 11-02 07:23 | +10 stop | ZEC | UP | 0.57 | 0.75 | 1.48 |
| 11-02 07:23 | +20 | ZEC | UP | 0.58 | 0.83 | 2.22 |
| 11-02 07:23 | +15 | ZEC | UP | 0.58 | 0.75 | 1.38 |
| 11-02 07:23 | +10 | ZEC | UP | 0.58 | 0.75 | 1.38 |
| 11-02 07:23 | +10 stop | SOL | UP | 0.54 | 0.72 | 1.47 |
| 11-02 07:23 | +20 | SOL | UP | 0.54 | 0.83 | 2.62 |
| 11-02 07:23 | +15 | SOL | UP | 0.54 | 0.72 | 1.47 |
| 11-02 07:23 | +10 | SOL | UP | 0.54 | 0.72 | 1.47 |
| 11-02 07:23 | +5 | SOL | UP | 0.54 | 0.72 | 1.47 |
| 11-02 07:23 | +10 stop | BTC | UP | 0.52 | 0.33 | -2.24 |
| 11-02 07:23 | +20 | BTC | UP | 0.52 | open |  |
| 11-02 07:23 | +15 | BTC | UP | 0.52 | open |  |
| 11-02 07:23 | +10 | BTC | UP | 0.51 | open |  |
| 11-02 07:23 | +5 | BTC | UP | 0.50 | 0.59 | 0.55 |
| 11-02 07:23 | +10 stop | ETH | UP | 0.51 | 0.34 | -2.04 |
| 11-02 07:23 | +20 | ETH | UP | 0.51 | open |  |
| 11-02 07:23 | +15 | ETH | UP | 0.51 | open |  |
| 11-02 07:23 | +10 | ETH | UP | 0.51 | open |  |
| 11-02 07:23 | +5 | ETH | UP | 0.51 | open |  |
| 11-02 07:21 | +10 stop | DOGE | UP | 0.61 | 0.33 | -3.13 |
