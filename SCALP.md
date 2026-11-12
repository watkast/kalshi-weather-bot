# Range-Scalp Bot

*Updated Thu Nov 12 20:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57261 | 49926 | 7335 (101) | 2 | $-15688.02 | -4.4% |
| **+10¢** | 42802 | 34241 | 8561 (133) | 3 | $-14624.27 | -5.4% |
| **+15¢** | 35885 | 26670 | 9215 (167) | 3 | $-13214.38 | -5.9% |
| **+20¢** | 31972 | 22303 | 9669 (217) | 3 | $-11574.51 | -5.8% |
| **+10¢ (15¢ stop)** | 69818 | 69690 | 128 (78) | 2 | $-25740.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 20:51 | +10 stop | NEAR | DOWN | 0.58 | open |  |
| 11-12 20:51 | +10 stop | DOGE | UP | 0.61 | open |  |
| 11-12 20:51 | +10 | DOGE | UP | 0.61 | open |  |
| 11-12 20:50 | +10 stop | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 11-12 20:50 | +5 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 11-12 20:50 | +10 stop | DOGE | DOWN | 0.47 | 0.61 | 1.05 |
| 11-12 20:50 | +10 | DOGE | DOWN | 0.47 | 0.61 | 1.05 |
| 11-12 20:50 | +5 | SOL | UP | 0.49 | 0.61 | 0.85 |
| 11-12 20:49 | +5 | DOGE | UP | 0.65 | open |  |
| 11-12 20:49 | +10 stop | NEAR | UP | 0.70 | 0.54 | -1.93 |
| 11-12 20:49 | +20 | NEAR | UP | 0.70 | open |  |
| 11-12 20:49 | +15 | NEAR | UP | 0.70 | open |  |
| 11-12 20:49 | +10 | NEAR | UP | 0.69 | open |  |
| 11-12 20:49 | +5 | NEAR | UP | 0.69 | open |  |
| 11-12 20:49 | +10 stop | SOL | UP | 0.58 | 0.42 | -1.96 |
| 11-12 20:49 | +20 | SOL | UP | 0.58 | open |  |
| 11-12 20:49 | +15 | SOL | UP | 0.58 | open |  |
| 11-12 20:49 | +10 | SOL | UP | 0.58 | open |  |
| 11-12 20:49 | +5 | SOL | UP | 0.58 | 0.66 | 0.46 |
| 11-12 20:49 | +10 stop | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 11-12 20:49 | +20 | DOGE | UP | 0.57 | open |  |
| 11-12 20:49 | +15 | DOGE | UP | 0.57 | open |  |
| 11-12 20:49 | +10 | DOGE | UP | 0.57 | 0.68 | 0.76 |
| 11-12 20:49 | +5 | DOGE | UP | 0.57 | 0.63 | 0.25 |
| 11-12 20:45 | +10 stop | ETH | UP | 0.63 | 0.77 | 1.10 |
| 11-12 20:45 | +20 | ETH | UP | 0.63 | 0.84 | 1.83 |
| 11-12 20:45 | +15 | ETH | UP | 0.63 | 0.78 | 1.20 |
| 11-12 20:45 | +10 | ETH | UP | 0.63 | 0.77 | 1.10 |
| 11-12 20:45 | +5 | ETH | UP | 0.63 | 0.77 | 1.10 |
| 11-12 20:45 | +10 stop | NEAR | UP | 0.67 | 0.86 | 1.65 |
| 11-12 20:45 | +20 | NEAR | UP | 0.67 | 0.87 | 1.76 |
| 11-12 20:45 | +15 | NEAR | UP | 0.67 | 0.86 | 1.65 |
| 11-12 20:45 | +10 | NEAR | UP | 0.67 | 0.86 | 1.65 |
| 11-12 20:45 | +5 | NEAR | UP | 0.67 | 0.76 | 0.61 |
| 11-12 20:43 | +10 stop | ETH | DOWN | 0.70 | 0.93 | 2.09 |
| 11-12 20:43 | +20 | ETH | DOWN | 0.70 | 0.93 | 2.09 |
| 11-12 20:43 | +15 | ETH | DOWN | 0.70 | 0.93 | 2.09 |
| 11-12 20:43 | +10 | ETH | DOWN | 0.70 | 0.93 | 2.09 |
| 11-12 20:43 | +5 | ETH | DOWN | 0.69 | 0.93 | 2.19 |
| 11-12 20:43 | +10 stop | BNB | UP | 0.68 | 0.82 | 1.13 |
