# Range-Scalp Bot

*Updated Sat Oct 31 06:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41861 | 36523 | 5338 (54) | 1 | $-11772.07 | -4.5% |
| **+10¢** | 31201 | 25021 | 6180 (78) | 1 | $-10541.47 | -5.4% |
| **+15¢** | 26084 | 19421 | 6663 (106) | 1 | $-9633.01 | -5.9% |
| **+20¢** | 23161 | 16184 | 6977 (137) | 3 | $-8487.15 | -5.8% |
| **+10¢ (15¢ stop)** | 51020 | 50945 | 75 (41) | 0 | $-19245.16 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 06:01 | +10 stop | BNB | UP | 0.64 | 0.76 | 0.90 |
| 10-31 06:01 | +20 | BNB | UP | 0.64 | open |  |
| 10-31 06:01 | +15 | BNB | UP | 0.62 | 0.78 | 1.30 |
| 10-31 06:01 | +10 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 10-31 06:01 | +5 | BNB | UP | 0.62 | 0.76 | 1.10 |
| 10-31 06:01 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-31 06:00 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 10-31 06:00 | +20 | ETH | UP | 0.69 | open |  |
| 10-31 06:00 | +15 | ETH | UP | 0.69 | 0.86 | 1.46 |
| 10-31 06:00 | +10 | ETH | UP | 0.70 | 0.80 | 0.74 |
| 10-31 06:00 | +5 | ETH | UP | 0.67 | 0.76 | 0.61 |
| 10-31 06:00 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-31 06:00 | +20 | DOGE | UP | 0.68 | 0.91 | 2.05 |
| 10-31 06:00 | +15 | DOGE | UP | 0.68 | 0.85 | 1.45 |
| 10-31 06:00 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 10-31 06:00 | +5 | DOGE | UP | 0.68 | 0.75 | 0.40 |
| 10-31 06:00 | +10 stop | HYPE | DOWN | 0.55 | 0.34 | -2.44 |
| 10-31 06:00 | +20 | HYPE | DOWN | 0.55 | open |  |
| 10-31 06:00 | +15 | HYPE | DOWN | 0.55 | open |  |
| 10-31 06:00 | +10 | HYPE | DOWN | 0.55 | open |  |
| 10-31 06:00 | +5 | HYPE | DOWN | 0.55 | open |  |
| 10-31 05:52 | +10 stop | XRP | DOWN | 0.52 | 0.31 | -2.43 |
| 10-31 05:52 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 10-31 05:50 | +5 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 10-31 05:50 | +10 stop | XRP | UP | 0.59 | 0.39 | -2.34 |
| 10-31 05:50 | +5 | XRP | UP | 0.59 | 0.68 | 0.57 |
| 10-31 05:49 | +10 stop | BNB | UP | 0.54 | 0.71 | 1.37 |
| 10-31 05:48 | +5 | XRP | UP | 0.56 | 0.67 | 0.76 |
| 10-31 05:48 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-31 05:48 | +5 | HYPE | DOWN | 0.68 | 0.79 | 0.78 |
| 10-31 05:48 | +10 stop | BNB | DOWN | 0.63 | 0.41 | -2.54 |
| 10-31 05:48 | +5 | BNB | DOWN | 0.63 | yes | -6.47 |
| 10-31 05:48 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 10-31 05:47 | +10 stop | NEAR | DOWN | 0.62 | 0.72 | 0.68 |
| 10-31 05:47 | +10 stop | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-31 05:47 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 10-31 05:47 | +10 stop | DOGE | DOWN | 0.56 | 0.40 | -1.95 |
| 10-31 05:47 | +20 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-31 05:47 | +15 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 10-31 05:47 | +10 | DOGE | DOWN | 0.56 | yes | -5.78 |
