# Range-Scalp Bot

*Updated Thu Nov 12 01:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56368 | 49143 | 7225 (98) | 1 | $-15481.98 | -4.4% |
| **+10¢** | 42124 | 33695 | 8429 (128) | 1 | $-14441.53 | -5.5% |
| **+15¢** | 35326 | 26243 | 9083 (162) | 1 | $-13134.04 | -5.9% |
| **+20¢** | 31473 | 21944 | 9529 (212) | 1 | $-11490.67 | -5.8% |
| **+10¢ (15¢ stop)** | 68695 | 68572 | 123 (73) | 0 | $-25344.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 01:09 | +10 stop | HYPE | DOWN | 0.60 | 0.84 | 2.13 |
| 11-12 01:09 | +15 | HYPE | DOWN | 0.60 | 0.84 | 2.13 |
| 11-12 01:09 | +10 | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-12 01:09 | +5 | HYPE | DOWN | 0.65 | 0.84 | 1.64 |
| 11-12 01:06 | +10 stop | NEAR | DOWN | 0.67 | 0.80 | 1.00 |
| 11-12 01:06 | +10 | NEAR | DOWN | 0.67 | 0.80 | 1.02 |
| 11-12 01:06 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-12 01:06 | +10 stop | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-12 01:04 | +10 stop | ZEC | DOWN | 0.59 | 0.73 | 1.09 |
| 11-12 01:03 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-12 01:03 | +20 | NEAR | DOWN | 0.64 | 0.89 | 2.26 |
| 11-12 01:03 | +15 | NEAR | DOWN | 0.64 | 0.80 | 1.31 |
| 11-12 01:03 | +10 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-12 01:03 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 11-12 01:03 | +10 stop | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 01:03 | +20 | HYPE | DOWN | 0.71 | 0.94 | 2.13 |
| 11-12 01:03 | +15 | HYPE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-12 01:03 | +10 | HYPE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 01:03 | +5 | HYPE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-12 01:03 | +10 stop | ZEC | UP | 0.54 | 0.33 | -2.44 |
| 11-12 01:03 | +20 | ZEC | UP | 0.54 | open |  |
| 11-12 01:03 | +15 | ZEC | UP | 0.54 | open |  |
| 11-12 01:03 | +10 | ZEC | UP | 0.54 | open |  |
| 11-12 01:03 | +5 | ZEC | UP | 0.54 | open |  |
| 11-12 01:02 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 01:02 | +20 | BNB | DOWN | 0.70 | 0.90 | 1.82 |
| 11-12 01:02 | +15 | BNB | DOWN | 0.70 | 0.89 | 1.68 |
| 11-12 01:02 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 01:02 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 11-12 01:02 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 01:02 | +20 | SOL | DOWN | 0.69 | 0.89 | 1.78 |
| 11-12 01:02 | +15 | SOL | DOWN | 0.69 | 0.88 | 1.67 |
| 11-12 01:02 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 11-12 01:02 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-11 23:34 | +10 stop | SOL | UP | 0.70 | no | -7.15 |
| 11-11 23:33 | +10 stop | SOL | UP | 0.71 | 0.55 | -1.91 |
| 11-11 23:33 | +5 | BNB | DOWN | 0.55 | no | 4.32 |
| 11-11 23:32 | +10 stop | XRP | UP | 0.65 | 0.78 | 1.01 |
| 11-11 23:32 | +10 stop | DOGE | UP | 0.69 | 0.88 | 1.67 |
| 11-11 23:32 | +10 stop | SOL | DOWN | 0.57 | 0.41 | -1.95 |
