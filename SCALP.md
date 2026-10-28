# Range-Scalp Bot

*Updated Wed Oct 28 17:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38233 | 33358 | 4875 (46) | 1 | $-10792.36 | -4.5% |
| **+10¢** | 28521 | 22888 | 5633 (68) | 1 | $-9590.38 | -5.3% |
| **+15¢** | 23866 | 17819 | 6047 (93) | 1 | $-8520.10 | -5.7% |
| **+20¢** | 21173 | 14840 | 6333 (118) | 1 | $-7476.14 | -5.6% |
| **+10¢ (15¢ stop)** | 46795 | 46728 | 67 (35) | 0 | $-17754.72 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 17:05 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-28 17:05 | +5 | SOL | DOWN | 0.70 | 0.75 | 0.21 |
| 10-28 17:02 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 10-28 17:02 | +10 stop | HYPE | UP | 0.49 | 0.26 | -2.66 |
| 10-28 17:02 | +20 | HYPE | UP | 0.50 | open |  |
| 10-28 17:02 | +15 | HYPE | UP | 0.51 | open |  |
| 10-28 17:02 | +10 | HYPE | UP | 0.51 | open |  |
| 10-28 17:02 | +5 | HYPE | UP | 0.51 | open |  |
| 10-28 17:02 | +10 stop | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 10-28 17:02 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 10-28 17:02 | +15 | BNB | DOWN | 0.67 | 0.84 | 1.44 |
| 10-28 17:02 | +10 | BNB | DOWN | 0.67 | 0.80 | 1.02 |
| 10-28 17:02 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.47 |
| 10-28 17:02 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-28 17:02 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 10-28 17:02 | +15 | DOGE | DOWN | 0.64 | 0.82 | 1.52 |
| 10-28 17:02 | +10 | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-28 17:02 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 10-28 17:01 | +10 stop | NEAR | DOWN | 0.69 | 0.54 | -1.83 |
| 10-28 17:01 | +20 | NEAR | DOWN | 0.69 | 0.90 | 1.90 |
| 10-28 17:01 | +15 | NEAR | DOWN | 0.69 | 0.84 | 1.25 |
| 10-28 17:01 | +10 | NEAR | DOWN | 0.69 | 0.82 | 1.04 |
| 10-28 17:01 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 10-28 17:01 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-28 17:01 | +20 | XRP | DOWN | 0.61 | 0.83 | 1.96 |
| 10-28 17:01 | +15 | XRP | DOWN | 0.61 | 0.76 | 1.23 |
| 10-28 17:01 | +10 | XRP | DOWN | 0.61 | 0.73 | 0.92 |
| 10-28 17:01 | +5 | XRP | DOWN | 0.61 | 0.73 | 0.92 |
| 10-28 17:01 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-28 17:01 | +20 | SOL | DOWN | 0.63 | 0.84 | 1.83 |
| 10-28 17:01 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-28 17:01 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-28 17:01 | +5 | SOL | DOWN | 0.63 | 0.70 | 0.38 |
| 10-28 17:00 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 17:00 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.93 |
| 10-28 17:00 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-28 17:00 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 17:00 | +5 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-28 17:00 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 10-28 17:00 | +20 | ZEC | DOWN | 0.70 | 0.92 | 2.01 |
