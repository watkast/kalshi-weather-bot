# Range-Scalp Bot

*Updated Tue Nov 24 06:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70496 | 61535 | 8961 (148) | 1 | $-18820.83 | -4.2% |
| **+10¢** | 52597 | 42134 | 10463 (192) | 1 | $-17419.17 | -5.3% |
| **+15¢** | 44063 | 32793 | 11270 (248) | 1 | $-15498.04 | -5.6% |
| **+20¢** | 39239 | 27374 | 11865 (314) | 1 | $-13855.85 | -5.6% |
| **+10¢ (15¢ stop)** | 85838 | 85640 | 198 (118) | 0 | $-31552.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 06:07 | +15 | ZEC | DOWN | 0.68 | 0.85 | 1.45 |
| 11-24 06:07 | +5 | ZEC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-24 06:06 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-24 06:06 | +10 stop | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-24 06:06 | +10 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 11-24 06:04 | +10 stop | ZEC | DOWN | 0.60 | 0.45 | -1.85 |
| 11-24 06:04 | +20 | ZEC | DOWN | 0.60 | 0.85 | 2.24 |
| 11-24 06:04 | +15 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-24 06:04 | +10 | ZEC | DOWN | 0.58 | 0.72 | 1.07 |
| 11-24 06:04 | +5 | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-24 06:01 | +10 stop | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-24 06:01 | +20 | BTC | DOWN | 0.71 | 0.93 | 2.01 |
| 11-24 06:01 | +15 | BTC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-24 06:01 | +10 | BTC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-24 06:01 | +5 | BTC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-24 06:01 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-24 06:01 | +20 | ZEC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-24 06:01 | +15 | ZEC | DOWN | 0.60 | 0.80 | 1.71 |
| 11-24 06:01 | +10 | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-24 06:01 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 11-24 06:00 | +10 stop | NEAR | UP | 0.57 | 0.31 | -2.93 |
| 11-24 06:00 | +20 | NEAR | UP | 0.57 | open |  |
| 11-24 06:00 | +15 | NEAR | UP | 0.57 | open |  |
| 11-24 06:00 | +10 | NEAR | UP | 0.57 | open |  |
| 11-24 06:00 | +5 | NEAR | UP | 0.57 | open |  |
| 11-24 05:57 | +10 stop | ZEC | DOWN | 0.67 | 0.38 | -3.23 |
| 11-24 05:55 | +10 stop | ZEC | UP | 0.53 | 0.22 | -3.41 |
| 11-24 05:54 | +10 stop | HYPE | DOWN | 0.62 | 0.79 | 1.41 |
| 11-24 05:53 | +10 stop | DOGE | DOWN | 0.61 | 0.86 | 2.24 |
| 11-24 05:53 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 11-24 05:53 | +5 | ZEC | UP | 0.65 | 0.93 | 2.60 |
| 11-24 05:53 | +10 stop | HYPE | UP | 0.55 | 0.32 | -2.64 |
| 11-24 05:53 | +10 stop | SOL | UP | 0.54 | 0.39 | -1.85 |
| 11-24 05:53 | +5 | SOL | UP | 0.60 | no | -6.15 |
| 11-24 05:52 | +5 | SOL | DOWN | 0.50 | 0.55 | 0.14 |
| 11-24 05:52 | +10 stop | DOGE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-24 05:51 | +5 | SOL | DOWN | 0.60 | 0.67 | 0.37 |
| 11-24 05:50 | +10 stop | HYPE | DOWN | 0.61 | 0.45 | -1.95 |
| 11-24 05:50 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-24 05:49 | +10 stop | BNB | DOWN | 0.56 | 0.71 | 1.19 |
