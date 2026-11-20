# Range-Scalp Bot

*Updated Fri Nov 20 17:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66429 | 57973 | 8456 (128) | 0 | $-17883.98 | -4.3% |
| **+10¢** | 49596 | 39709 | 9887 (170) | 1 | $-16661.20 | -5.3% |
| **+15¢** | 41591 | 30930 | 10661 (217) | 1 | $-14980.88 | -5.7% |
| **+20¢** | 37034 | 25838 | 11196 (273) | 2 | $-13262.62 | -5.7% |
| **+10¢ (15¢ stop)** | 80887 | 80721 | 166 (100) | 1 | $-29866.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 17:02 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 11-20 17:02 | +20 | ZEC | DOWN | 0.70 | open |  |
| 11-20 17:02 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-20 17:02 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-20 17:02 | +5 | ZEC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-20 17:01 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-20 17:01 | +20 | BNB | DOWN | 0.69 | 0.89 | 1.78 |
| 11-20 17:01 | +15 | BNB | DOWN | 0.69 | 0.88 | 1.67 |
| 11-20 17:01 | +10 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 11-20 17:01 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.30 |
| 11-20 17:01 | +10 stop | BTC | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 17:01 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-20 17:01 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-20 17:01 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-20 17:01 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-20 17:01 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-20 17:01 | +5 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-20 16:58 | +10 stop | BTC | DOWN | 0.59 | 0.34 | -2.83 |
| 11-20 16:58 | +20 | BTC | DOWN | 0.57 | yes | -5.88 |
| 11-20 16:58 | +15 | BTC | DOWN | 0.58 | yes | -5.98 |
| 11-20 16:58 | +10 | BTC | DOWN | 0.58 | yes | -5.98 |
| 11-20 16:58 | +5 | BTC | DOWN | 0.54 | 0.61 | 0.35 |
| 11-20 16:57 | +10 stop | SOL | DOWN | 0.44 | 0.64 | 1.65 |
| 11-20 16:56 | +10 stop | ETH | DOWN | 0.55 | 0.35 | -2.33 |
| 11-20 16:56 | +5 | ETH | DOWN | 0.59 | yes | -6.07 |
| 11-20 16:56 | +10 stop | ETH | UP | 0.60 | 0.37 | -2.64 |
| 11-20 16:56 | +5 | ETH | UP | 0.59 | 0.68 | 0.57 |
| 11-20 16:55 | +10 stop | BTC | DOWN | 0.71 | 0.49 | -2.53 |
| 11-20 16:55 | +10 stop | SOL | UP | 0.47 | 0.58 | 0.74 |
| 11-20 16:54 | +10 stop | BTC | UP | 0.43 | 0.59 | 1.25 |
| 11-20 16:54 | +10 stop | ETH | UP | 0.71 | 0.56 | -1.83 |
| 11-20 16:54 | +10 stop | SOL | UP | 0.70 | 0.54 | -1.93 |
| 11-20 16:54 | +10 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-20 16:54 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-20 16:53 | +10 stop | SOL | DOWN | 0.46 | 0.58 | 0.84 |
| 11-20 16:53 | +10 stop | ETH | DOWN | 0.47 | 0.59 | 0.85 |
| 11-20 16:52 | +10 stop | BNB | DOWN | 0.70 | 0.55 | -1.83 |
| 11-20 16:52 | +5 | ETH | UP | 0.65 | 0.72 | 0.38 |
| 11-20 16:51 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-20 16:51 | +10 stop | BTC | UP | 0.69 | 0.51 | -2.13 |
