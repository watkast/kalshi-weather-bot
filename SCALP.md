# Range-Scalp Bot

*Updated Wed Nov 25 17:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71797 | 62661 | 9136 (158) | 2 | $-19162.83 | -4.2% |
| **+10¢** | 53555 | 42890 | 10665 (203) | 4 | $-17742.13 | -5.3% |
| **+15¢** | 44850 | 33366 | 11484 (260) | 8 | $-15803.34 | -5.6% |
| **+20¢** | 39934 | 27841 | 12093 (326) | 9 | $-14177.30 | -5.7% |
| **+10¢ (15¢ stop)** | 87435 | 87226 | 209 (128) | 0 | $-32113.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 17:03 | +10 stop | ETH | UP | 0.70 | 0.83 | 1.05 |
| 11-25 17:03 | +15 | ETH | UP | 0.71 | 0.88 | 1.47 |
| 11-25 17:03 | +10 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 11-25 17:03 | +5 | ETH | UP | 0.71 | 0.83 | 0.95 |
| 11-25 17:02 | +10 stop | ZEC | UP | 0.55 | 0.77 | 1.89 |
| 11-25 17:02 | +10 stop | SOL | UP | 0.63 | 0.85 | 1.94 |
| 11-25 17:02 | +10 stop | BNB | UP | 0.64 | 0.78 | 1.10 |
| 11-25 17:02 | +10 stop | BTC | UP | 0.63 | 0.81 | 1.52 |
| 11-25 17:02 | +10 | BTC | UP | 0.63 | 0.81 | 1.52 |
| 11-25 17:02 | +5 | BTC | UP | 0.63 | 0.81 | 1.52 |
| 11-25 17:02 | +10 stop | DOGE | UP | 0.60 | 0.86 | 2.36 |
| 11-25 17:02 | +10 | DOGE | UP | 0.60 | 0.86 | 2.36 |
| 11-25 17:02 | +5 | DOGE | UP | 0.60 | 0.68 | 0.49 |
| 11-25 17:02 | +10 stop | XRP | UP | 0.61 | 0.79 | 1.51 |
| 11-25 17:02 | +10 | XRP | UP | 0.61 | 0.79 | 1.51 |
| 11-25 17:02 | +5 | XRP | UP | 0.62 | 0.79 | 1.41 |
| 11-25 17:02 | +10 stop | HYPE | UP | 0.56 | 0.74 | 1.48 |
| 11-25 17:02 | +10 | HYPE | UP | 0.56 | 0.74 | 1.48 |
| 11-25 17:02 | +5 | HYPE | UP | 0.56 | 0.74 | 1.48 |
| 11-25 17:02 | +10 stop | NEAR | UP | 0.64 | 0.85 | 1.84 |
| 11-25 17:02 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 11-25 17:02 | +5 | SOL | UP | 0.62 | 0.71 | 0.58 |
| 11-25 17:01 | +10 stop | ETH | DOWN | 0.52 | 0.66 | 1.06 |
| 11-25 17:01 | +20 | ETH | DOWN | 0.52 | open |  |
| 11-25 17:01 | +15 | ETH | DOWN | 0.51 | 0.66 | 1.16 |
| 11-25 17:01 | +10 | ETH | DOWN | 0.51 | 0.66 | 1.16 |
| 11-25 17:01 | +5 | ETH | DOWN | 0.51 | 0.66 | 1.16 |
| 11-25 17:01 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-25 17:01 | +20 | BTC | DOWN | 0.58 | open |  |
| 11-25 17:01 | +15 | BTC | DOWN | 0.58 | open |  |
| 11-25 17:01 | +10 | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-25 17:01 | +5 | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-25 17:01 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 11-25 17:01 | +20 | HYPE | DOWN | 0.55 | open |  |
| 11-25 17:01 | +15 | HYPE | DOWN | 0.55 | open |  |
| 11-25 17:01 | +10 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-25 17:01 | +5 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-25 17:01 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-25 17:01 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-25 17:01 | +15 | DOGE | DOWN | 0.58 | open |  |
