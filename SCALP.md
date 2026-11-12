# Range-Scalp Bot

*Updated Thu Nov 12 05:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56699 | 49428 | 7271 (98) | 4 | $-15622.24 | -4.4% |
| **+10¢** | 42373 | 33891 | 8482 (128) | 4 | $-14563.32 | -5.5% |
| **+15¢** | 35524 | 26392 | 9132 (162) | 5 | $-13208.54 | -5.9% |
| **+20¢** | 31643 | 22060 | 9583 (212) | 7 | $-11605.16 | -5.8% |
| **+10¢ (15¢ stop)** | 69133 | 69010 | 123 (73) | 0 | $-25553.69 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 05:35 | +5 | NEAR | UP | 0.46 | 0.57 | 0.74 |
| 11-12 05:35 | +5 | BNB | DOWN | 0.56 | open |  |
| 11-12 05:35 | +10 stop | BNB | DOWN | 0.57 | 0.27 | -3.32 |
| 11-12 05:35 | +5 | BNB | DOWN | 0.57 | 0.65 | 0.46 |
| 11-12 05:35 | +10 stop | DOGE | DOWN | 0.51 | 0.23 | -3.11 |
| 11-12 05:35 | +5 | DOGE | DOWN | 0.51 | 0.60 | 0.55 |
| 11-12 05:35 | +10 stop | ETH | DOWN | 0.55 | 0.38 | -2.05 |
| 11-12 05:35 | +10 stop | XRP | DOWN | 0.51 | 0.35 | -1.94 |
| 11-12 05:35 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-12 05:35 | +5 | XRP | DOWN | 0.52 | open |  |
| 11-12 05:34 | +10 stop | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-12 05:34 | +20 | XRP | UP | 0.49 | open |  |
| 11-12 05:34 | +15 | XRP | UP | 0.49 | 0.64 | 1.15 |
| 11-12 05:34 | +10 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-12 05:34 | +5 | XRP | UP | 0.49 | 0.60 | 0.75 |
| 11-12 05:34 | +10 stop | BNB | DOWN | 0.54 | 0.65 | 0.76 |
| 11-12 05:34 | +10 stop | DOGE | DOWN | 0.56 | 0.68 | 0.86 |
| 11-12 05:34 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
| 11-12 05:34 | +10 stop | SOL | UP | 0.60 | 0.70 | 0.68 |
| 11-12 05:34 | +20 | SOL | UP | 0.60 | 0.85 | 2.24 |
| 11-12 05:34 | +15 | SOL | UP | 0.60 | 0.76 | 1.30 |
| 11-12 05:34 | +10 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 11-12 05:34 | +5 | SOL | UP | 0.61 | 0.69 | 0.48 |
| 11-12 05:34 | +5 | DOGE | DOWN | 0.55 | 0.68 | 0.96 |
| 11-12 05:34 | +10 stop | NEAR | UP | 0.53 | 0.66 | 0.96 |
| 11-12 05:34 | +20 | NEAR | UP | 0.53 | open |  |
| 11-12 05:34 | +15 | NEAR | UP | 0.53 | open |  |
| 11-12 05:34 | +10 | NEAR | UP | 0.53 | 0.66 | 0.96 |
| 11-12 05:34 | +5 | NEAR | UP | 0.53 | 0.58 | 0.14 |
| 11-12 05:34 | +10 stop | ZEC | UP | 0.62 | 0.45 | -2.05 |
| 11-12 05:34 | +20 | ZEC | UP | 0.62 | 0.86 | 2.14 |
| 11-12 05:34 | +15 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 11-12 05:34 | +10 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 11-12 05:34 | +5 | ZEC | UP | 0.62 | 0.77 | 1.20 |
| 11-12 05:34 | +10 stop | ETH | UP | 0.53 | 0.32 | -2.44 |
| 11-12 05:34 | +20 | ETH | UP | 0.56 | open |  |
| 11-12 05:34 | +15 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-12 05:34 | +10 | ETH | UP | 0.56 | 0.72 | 1.27 |
| 11-12 05:34 | +5 | ETH | UP | 0.56 | 0.61 | 0.15 |
| 11-12 05:34 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
