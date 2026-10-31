# Range-Scalp Bot

*Updated Sat Oct 31 01:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41541 | 36253 | 5288 (54) | 7 | $-11619.68 | -4.4% |
| **+10¢** | 30963 | 24843 | 6120 (78) | 7 | $-10363.27 | -5.3% |
| **+15¢** | 25882 | 19286 | 6596 (106) | 7 | $-9430.33 | -5.8% |
| **+20¢** | 22975 | 16068 | 6907 (137) | 7 | $-8297.38 | -5.8% |
| **+10¢ (15¢ stop)** | 50635 | 50560 | 75 (41) | 1 | $-19145.96 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 01:27 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-31 01:23 | +10 stop | DOGE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-31 01:23 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-31 01:23 | +10 stop | ZEC | DOWN | 0.64 | 0.80 | 1.31 |
| 10-31 01:23 | +10 stop | BNB | UP | 0.57 | 0.18 | -4.19 |
| 10-31 01:21 | +5 | SOL | UP | 0.68 | open |  |
| 10-31 01:21 | +10 stop | DOGE | UP | 0.60 | 0.33 | -3.03 |
| 10-31 01:21 | +10 stop | BTC | UP | 0.60 | 0.35 | -2.83 |
| 10-31 01:20 | +15 | SOL | UP | 0.58 | open |  |
| 10-31 01:20 | +10 | SOL | UP | 0.58 | open |  |
| 10-31 01:20 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 10-31 01:20 | +10 stop | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-31 01:20 | +20 | NEAR | DOWN | 0.59 | 0.81 | 1.92 |
| 10-31 01:20 | +15 | NEAR | DOWN | 0.59 | 0.81 | 1.92 |
| 10-31 01:20 | +10 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 10-31 01:20 | +5 | NEAR | DOWN | 0.59 | 0.65 | 0.27 |
| 10-31 01:20 | +10 stop | HYPE | DOWN | 0.71 | 0.49 | -2.53 |
| 10-31 01:20 | +10 stop | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-31 01:20 | +10 stop | DOGE | DOWN | 0.65 | 0.43 | -2.54 |
| 10-31 01:19 | +10 | SOL | UP | 0.55 | 0.65 | 0.66 |
| 10-31 01:19 | +10 stop | SOL | UP | 0.59 | 0.27 | -3.48 |
| 10-31 01:19 | +5 | SOL | UP | 0.58 | 0.63 | 0.15 |
| 10-31 01:18 | +10 stop | SOL | UP | 0.49 | 0.59 | 0.65 |
| 10-31 01:18 | +20 | SOL | UP | 0.49 | open |  |
| 10-31 01:18 | +15 | SOL | UP | 0.49 | 0.65 | 1.26 |
| 10-31 01:18 | +10 | SOL | UP | 0.50 | 0.63 | 0.95 |
| 10-31 01:18 | +5 | SOL | UP | 0.50 | 0.59 | 0.55 |
| 10-31 01:18 | +10 stop | XRP | UP | 0.55 | 0.38 | -2.05 |
| 10-31 01:18 | +20 | XRP | UP | 0.55 | open |  |
| 10-31 01:18 | +15 | XRP | UP | 0.55 | open |  |
| 10-31 01:18 | +10 | XRP | UP | 0.55 | open |  |
| 10-31 01:18 | +5 | XRP | UP | 0.55 | open |  |
| 10-31 01:18 | +10 stop | HYPE | UP | 0.60 | 0.34 | -2.93 |
| 10-31 01:18 | +20 | HYPE | UP | 0.60 | open |  |
| 10-31 01:18 | +15 | HYPE | UP | 0.60 | open |  |
| 10-31 01:18 | +10 | HYPE | UP | 0.60 | open |  |
| 10-31 01:18 | +5 | HYPE | UP | 0.60 | open |  |
| 10-31 01:18 | +10 stop | ETH | UP | 0.62 | 0.40 | -2.54 |
| 10-31 01:18 | +20 | ETH | UP | 0.62 | open |  |
| 10-31 01:18 | +15 | ETH | UP | 0.62 | open |  |
