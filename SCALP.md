# Range-Scalp Bot

*Updated Mon Nov 02 00:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44116 | 38423 | 5693 (65) | 0 | $-12715.18 | -4.6% |
| **+10¢** | 32923 | 26343 | 6580 (86) | 0 | $-11481.20 | -5.5% |
| **+15¢** | 27555 | 20473 | 7082 (113) | 0 | $-10494.11 | -6.1% |
| **+20¢** | 24481 | 17066 | 7415 (147) | 0 | $-9237.01 | -6.0% |
| **+10¢ (15¢ stop)** | 53804 | 53718 | 86 (51) | 0 | $-20347.47 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
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
| 11-02 00:09 | +5 | DOGE | UP | 0.65 | no | -6.66 |
| 11-02 00:09 | +10 stop | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-02 00:09 | +10 | HYPE | DOWN | 0.62 | 0.76 | 1.06 |
| 11-02 00:09 | +5 | HYPE | DOWN | 0.62 | 0.71 | 0.54 |
| 11-02 00:09 | +10 stop | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 11-02 00:08 | +10 stop | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 00:08 | +10 | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 00:08 | +5 | HYPE | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 00:08 | +10 stop | ETH | UP | 0.61 | 0.40 | -2.44 |
| 11-02 00:08 | +20 | ETH | UP | 0.61 | no | -6.27 |
| 11-02 00:08 | +15 | ETH | UP | 0.61 | no | -6.27 |
| 11-02 00:08 | +10 | ETH | UP | 0.61 | no | -6.27 |
| 11-02 00:08 | +5 | ETH | UP | 0.61 | 0.68 | 0.37 |
| 11-02 00:08 | +5 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-02 00:07 | +10 stop | BTC | DOWN | 0.52 | 0.71 | 1.57 |
| 11-02 00:07 | +10 stop | SOL | UP | 0.69 | 0.46 | -2.63 |
| 11-02 00:07 | +20 | SOL | UP | 0.69 | no | -7.05 |
| 11-02 00:07 | +15 | SOL | UP | 0.68 | no | -6.96 |
| 11-02 00:07 | +10 | SOL | UP | 0.68 | no | -6.96 |
| 11-02 00:07 | +5 | SOL | UP | 0.68 | no | -6.96 |
| 11-02 00:06 | +10 stop | NEAR | UP | 0.48 | 0.32 | -1.94 |
| 11-02 00:06 | +20 | NEAR | UP | 0.48 | no | -4.98 |
| 11-02 00:06 | +15 | NEAR | UP | 0.48 | no | -4.98 |
| 11-02 00:06 | +10 | NEAR | UP | 0.48 | no | -4.98 |
| 11-02 00:06 | +5 | NEAR | UP | 0.48 | 0.54 | 0.24 |
| 11-02 00:06 | +10 stop | BTC | UP | 0.60 | 0.45 | -1.85 |
