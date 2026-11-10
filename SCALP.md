# Range-Scalp Bot

*Updated Tue Nov 10 05:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54224 | 47299 | 6925 (89) | 2 | $-14785.00 | -4.3% |
| **+10¢** | 40512 | 32433 | 8079 (117) | 2 | $-13727.18 | -5.4% |
| **+15¢** | 33954 | 25245 | 8709 (150) | 2 | $-12489.97 | -5.9% |
| **+20¢** | 30234 | 21098 | 9136 (198) | 2 | $-10897.63 | -5.7% |
| **+10¢ (15¢ stop)** | 66062 | 65952 | 110 (66) | 0 | $-24428.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 05:09 | +10 stop | BNB | UP | 0.70 | 0.84 | 1.15 |
| 11-10 05:09 | +10 stop | BTC | UP | 0.63 | 0.81 | 1.52 |
| 11-10 05:06 | +10 stop | BTC | DOWN | 0.66 | 0.45 | -2.44 |
| 11-10 05:06 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-10 05:06 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-10 05:06 | +10 stop | BNB | DOWN | 0.53 | 0.34 | -2.24 |
| 11-10 05:05 | +10 stop | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 11-10 05:05 | +15 | ZEC | UP | 0.69 | 0.87 | 1.57 |
| 11-10 05:05 | +10 | ZEC | UP | 0.69 | 0.80 | 0.83 |
| 11-10 05:05 | +5 | ZEC | UP | 0.69 | 0.74 | 0.21 |
| 11-10 05:05 | +10 stop | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-10 05:05 | +20 | BTC | DOWN | 0.60 | open |  |
| 11-10 05:05 | +15 | BTC | DOWN | 0.60 | open |  |
| 11-10 05:05 | +10 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-10 05:05 | +5 | BTC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-10 05:05 | +10 stop | BNB | UP | 0.57 | 0.39 | -2.15 |
| 11-10 05:05 | +10 stop | ETH | UP | 0.61 | 0.75 | 1.09 |
| 11-10 05:05 | +20 | ETH | UP | 0.61 | 0.87 | 2.35 |
| 11-10 05:05 | +15 | ETH | UP | 0.61 | 0.80 | 1.61 |
| 11-10 05:05 | +10 | ETH | UP | 0.61 | 0.75 | 1.09 |
| 11-10 05:05 | +5 | ETH | UP | 0.61 | 0.75 | 1.09 |
| 11-10 05:02 | +10 stop | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:02 | +20 | BTC | UP | 0.65 | 0.86 | 1.85 |
| 11-10 05:02 | +15 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:02 | +10 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:02 | +5 | BTC | UP | 0.65 | 0.84 | 1.64 |
| 11-10 05:01 | +10 stop | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +20 | ZEC | UP | 0.69 | 0.91 | 2.00 |
| 11-10 05:01 | +15 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +10 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +5 | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 11-10 05:01 | +10 stop | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-10 05:01 | +20 | ETH | UP | 0.59 | 0.82 | 2.02 |
| 11-10 05:01 | +15 | ETH | UP | 0.59 | 0.75 | 1.29 |
| 11-10 05:01 | +10 | ETH | UP | 0.59 | 0.73 | 1.09 |
| 11-10 05:01 | +5 | ETH | UP | 0.59 | 0.65 | 0.27 |
| 11-10 05:00 | +10 stop | BNB | DOWN | 0.56 | 0.28 | -3.18 |
| 11-10 05:00 | +20 | BNB | DOWN | 0.56 | open |  |
| 11-10 05:00 | +15 | BNB | DOWN | 0.56 | open |  |
| 11-10 05:00 | +10 | BNB | DOWN | 0.56 | open |  |
