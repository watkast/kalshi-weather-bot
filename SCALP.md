# Range-Scalp Bot

*Updated Fri Oct 30 21:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41317 | 36063 | 5254 (54) | 4 | $-11520.42 | -4.4% |
| **+10¢** | 30795 | 24716 | 6079 (78) | 6 | $-10251.66 | -5.3% |
| **+15¢** | 25740 | 19190 | 6550 (106) | 6 | $-9300.67 | -5.8% |
| **+20¢** | 22844 | 15984 | 6860 (137) | 6 | $-8177.78 | -5.7% |
| **+10¢ (15¢ stop)** | 50376 | 50301 | 75 (41) | 0 | $-19035.02 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 21:50 | +10 stop | NEAR | DOWN | 0.68 | 0.83 | 1.24 |
| 10-30 21:50 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 10-30 21:49 | +10 stop | SOL | DOWN | 0.59 | 0.83 | 2.13 |
| 10-30 21:48 | +10 stop | BTC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 21:48 | +10 stop | XRP | DOWN | 0.61 | 0.71 | 0.68 |
| 10-30 21:48 | +5 | NEAR | UP | 0.57 | 0.63 | 0.25 |
| 10-30 21:48 | +10 stop | BNB | UP | 0.52 | 0.36 | -1.95 |
| 10-30 21:48 | +15 | BNB | UP | 0.52 | open |  |
| 10-30 21:48 | +10 | BNB | UP | 0.52 | open |  |
| 10-30 21:48 | +5 | BNB | UP | 0.52 | open |  |
| 10-30 21:48 | +5 | BTC | UP | 0.57 | open |  |
| 10-30 21:48 | +10 stop | ETH | DOWN | 0.64 | 0.75 | 0.79 |
| 10-30 21:48 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-30 21:48 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.78 |
| 10-30 21:48 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-30 21:48 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-30 21:48 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-30 21:48 | +5 | ETH | DOWN | 0.65 | 0.75 | 0.70 |
| 10-30 21:47 | +10 stop | SOL | UP | 0.59 | 0.40 | -2.24 |
| 10-30 21:47 | +10 | SOL | UP | 0.60 | open |  |
| 10-30 21:47 | +5 | SOL | UP | 0.60 | open |  |
| 10-30 21:47 | +5 | BTC | UP | 0.54 | 0.66 | 0.86 |
| 10-30 21:46 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 10-30 21:46 | +20 | DOGE | DOWN | 0.59 | 0.80 | 1.81 |
| 10-30 21:46 | +15 | DOGE | DOWN | 0.59 | 0.76 | 1.44 |
| 10-30 21:46 | +10 | DOGE | DOWN | 0.59 | 0.69 | 0.72 |
| 10-30 21:46 | +5 | DOGE | DOWN | 0.59 | 0.69 | 0.72 |
| 10-30 21:46 | +10 stop | ETH | UP | 0.60 | 0.45 | -1.85 |
| 10-30 21:46 | +20 | ETH | UP | 0.60 | open |  |
| 10-30 21:46 | +15 | ETH | UP | 0.60 | open |  |
| 10-30 21:46 | +10 | ETH | UP | 0.60 | open |  |
| 10-30 21:46 | +5 | ETH | UP | 0.60 | 0.65 | 0.17 |
| 10-30 21:46 | +10 stop | NEAR | UP | 0.62 | 0.47 | -1.85 |
| 10-30 21:46 | +20 | NEAR | UP | 0.62 | open |  |
| 10-30 21:46 | +15 | NEAR | UP | 0.62 | open |  |
| 10-30 21:46 | +10 | NEAR | UP | 0.62 | open |  |
| 10-30 21:46 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 10-30 21:46 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-30 21:46 | +20 | HYPE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-30 21:46 | +15 | HYPE | DOWN | 0.61 | 0.78 | 1.40 |
